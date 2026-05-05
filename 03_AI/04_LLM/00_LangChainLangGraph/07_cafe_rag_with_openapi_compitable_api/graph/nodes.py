from llm.chat_model import load_model
from graph.state import CafeState
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
import retrieval
from langgraph.config import get_stream_writer

async def intent_classify_node(state:CafeState):
    
    writer = get_stream_writer()
    writer("사용자의 질문 의도를 파악중입니다...\n")
    
    prompt_file_path = "prompts/intent_classify_v1.0.txt"
    with open(prompt_file_path, "r", encoding="utf-8") as f:
        prompt = PromptTemplate.from_template(f.read())
    chain = prompt | load_model(streaming=False) | JsonOutputParser()
    response = await chain.ainvoke({"query":state["query"]})
    
    writer(f"사용자의 질문 의도는 {response['intent']}로 판단됩니다.\n")
    
    return {"intent":response["intent"], "intent_reason":response["reason"]}

def retrieve_node(state:CafeState):
    writer = get_stream_writer()
    writer("사용자의 질문에 참고할 수 있는 문서를 검색중입니다...\n")
    document = retrieval.retrieve(query = state["query"])
    return {"document":document}

async def llm_node(state:CafeState):
    prompt_file_path = "prompts/llm_response_v1.0.txt"
    with open(prompt_file_path, "r", encoding="utf-8") as f:
        prompt = PromptTemplate.from_template(f.read())
    chain = prompt | load_model(streaming=True) | StrOutputParser()
    response = await chain.ainvoke({"query":state["query"], "reference":state["document"]})
    return {"response":response}

def fallback_node(state:CafeState):
    return {"response":"카페 이용 및 브랜드 관련 문의만 가능합니다. 다시 질문해주시기 바랍니다."}

def output_node(state:CafeState):
    return {"response" : state["response"]}