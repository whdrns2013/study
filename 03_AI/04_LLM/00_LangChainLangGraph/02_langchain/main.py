from fastapi import FastAPI
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
from typing import List, Union

# API 키 세팅 메서드
def set_api_key():
    from config.secret import secret
    import os
    os.environ["OPENAI_API_KEY"] = secret["apikey"]["openai"]
    os.environ["GOOGLE_API_KEY"] = secret["apikey"]["google"]
set_api_key()

# FastAPI
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

# OpenAI 라우터 추가
add_routes(
    app,
    ChatOpenAI(model="gpt-4o-mini"),
    path="/openai",
)

# Gemini 라우터 추가
add_routes(
    app,
    ChatGoogleGenerativeAI(model="gemini-2.5-flash"),
    path="/gemini",
)

# joke 라우터 추가
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
add_routes(
    app,
    prompt | model,
    path="/joke",
)

# playground=chat 모드
class InputChat(BaseModel):
    messages: List[Union[HumanMessage, AIMessage, SystemMessage]] = Field(
        ...,
        description="The chat messages representing the current conversation.",
    )
chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", streaming=True) # Playground Chat 모드에서는 streaming 옵션을 필수
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="messages"),
])
chat_parser = StrOutputParser()
chain = chat_prompt | chat_model | chat_parser
add_routes(
    app,
    chain.with_types(input_type=InputChat),
    path="/chat_ai",
    playground_type="chat" # playground_type = chat
)

# 파일 실행시
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)