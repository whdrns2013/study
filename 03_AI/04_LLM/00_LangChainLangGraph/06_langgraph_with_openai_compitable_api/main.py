import time
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import json
import uvicorn
import random
from graph.builder import UpDownGameGraph

app = FastAPI()

model_list = ["up-down-game"]

# /v1/models
@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": model,
                "object": "model",
                "created": int(time.time()),
                "owned_by": "local"
            } for model in model_list
        ]
    }

# /v1/chat/completions
@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    body = await request.json()
		
	# 요청 파라미터
    model = body.get("model", model_list[0])
    messages = body.get("messages", [])
    stream = body.get("stream", False)

    # 가장 마지막 user 메시지 추출
    user_message = ""
    for msg in reversed(messages):
        if msg.get("role") == "user":
            user_message = msg.get("content", "")
            break

    # LangGraph 애플리케이션 빌드
    app, graph = UpDownGameGraph.build()
    input_value = int(user_message)
    input_state = {"input":int(input_value), "count":0}

    # LangGraph 호출 예시
    ## 1. stream == false 인 경우
    if not stream:
        last_state = app.invoke(input_state)
        response = last_state["response"]
        return {
            "id": f"chatcmpl-{uuid.uuid4().hex}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": model,
            "choices": [
                {
                    "index":0,
                    "messages": {
                        "role": "assistant",
                        "content": response
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            }
        }

    ## 2. stream != false 인 경우
    async def event_generator():
        response_id = f"chatcmpl-{uuid.uuid4().hex}"
        created = int(time.time())
        
        ### 1) 첫 chunk : assistant role 알림
        first_chunk = {
            "id": response_id,
            "object": "chat.completion.chunk",
            "created": created,
            "model": model,
            "choices": [
                {
                    "index": 0,
                    "delta": {
                        "role": "assistant"
                    },
                    "finish_reason": None
                }
            ]
        }
        yield f"data: {json.dumps(first_chunk, ensure_ascii=False)}\n\n"
        
        ### 2) 중간 chunk : content (실제 답변)
        for token in app.stream(input_state, stream_mode="custom"):
            chunk = {
                "id": response_id,
                "object": "chat.completion.chunk",
                "created": created,
                "model": model,
                "choices": [
                    {
                        "index": 0,
                        "delta": {
                            "content": token
                            },
                        "finish_reason": None
                    }
                ]
            }
            yield f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n"
            # ensure_ascii=False : json dumps에서 한글을 \uXXX로 이스케이프 하지 않고 그대로 보내기 위한 옵션
            # \n\n : SSE에서 "이 이벤트 하나가 끝났다"라는 구분자. 반드시 필요.
        
        ### 3) 종료 chunk
        done_chunk = {
            "id": response_id,
            "object": "chat.completion.chunk",
            "created": created,
            "model": model,
            "choices": [
                {
                    "index": 0,
                    "delta": {}, # 빈 delta
                    "finish_reason": "stop"
                }
            ]
        }
        yield f"data: {json.dumps(done_chunk, ensure_ascii=False)}\n\n"
        
        ### 4) 종료 신호
        yield "data: [DONE]\n\n"
    
    return StreamingResponse(
        event_generator(),                # 스트리밍 제너레이터 
        media_type="text/event-stream"    # 미디어 타입
    )

# fastapi
def main():
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

# terminal
# def main():
#     while True:
#         app, graph = UpDownGameGraph.build()
#         user_input = int(input("숫자를 입력해주세요 : "))
#         for token in app.stream({"input":user_input, "count":0}, stream_mode="custom"):
#             print(token)

if __name__ == "__main__":
    main()
