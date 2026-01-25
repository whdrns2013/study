from google import genai
from core.config import config

def gemini(prompt:str):
    # 1. 클라이언트 초기화 (발급받은 API 키 입력)
    client = genai.Client(api_key=config["apikey"]["gemini"])

    # 2. 메시지 전송 및 응답 받기
    response = client.models.generate_content(
        model="gemini-2.5-flash", # 사용하고자 하는 모델명
        contents=prompt
    )

    # 3. 결과 출력
    return response


# 결과에서 텍스트 출력
# response.text

# TODO: OpenAI 와 같이 메시지 형식 처리
# TODO: 스트리밍 적용