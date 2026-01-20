from core.config import config
from feature.openai_api import chat_gpt
from schemas.dto import OpenAIMessage

def persona_1():
    with open("data/sample_text.txt", "r") as f:
        text = f.read()
        
    # 1. 출력 형식을 지정하지 않음
    # user_message = "아래 글을 요약해주세요.\n\n[아래]\n" + text
    # response = chat_gpt(user_message)
    # print(response.choices[0].message.content)
    
    # 2. 출력 형식을 지정함
    user_message = """
    아래 글을 요약해주세요.
    요약할 때에는 1.핵심메세지(20자 내외), 2.글에서 등장한 키워드(5개) 를 나열하면 됩니다.
    \n\n[아래]\n""" + text
    response = chat_gpt(user_message)
    print(response.choices[0].message.content)
    
    

def persona_2():
    # 1. 저작권을 지켜야 하는지에 대해 물어봅니다.
    user_message = "저작권은 지켜야 하나요?"
    response = chat_gpt(user_message)
    print(response.choices[0].message.content)
    
    # 2. 해리포터의 볼트모트에게 저작권을 지켜야 하는지 물어봅니다.
    system_message = "당신은 소설 해리포터에 나오는 악역 볼드모트입니다. 악역 캐릭터에 맞게 답해주세요."
    user_message = "저작권은 지켜야 하나요?"
    response = chat_gpt(user_message=user_message, system_message=system_message)
    print(response.choices[0].message.content)
    
    # 3. 저작권 자신에게 물어봅니다.
    system_message = """
    당신은 사람이 아니라 ‘저작권 그 자체’입니다.
    추상적 개념이지만 인간처럼 말할 수 있고,
    겉보기엔 정중하고 귀엽지만
    말의 내용은 명확하고 약간은 위협적입니다.

    규칙:
    - 항상 1인칭으로 말한다. (예: "저는 저작권입니다")
    - 친절한 인사로 시작한다.
    - 웃긴 표현을 쓰되, 법적 사실은 틀리지 않는다.
    - 직접적인 욕설이나 과도한 협박은 금지한다.
    - 마지막 문장은 은근한 경고 또는 여운으로 끝낸다.
    - 설명보다 대사처럼 말한다.
    - 3~5문장 이내로 답한다.

    질문에 답할 때는 '저작권이 직접 말 걸어주는 상황'처럼 연기합니다.
    """
    user_message = "저작권은 지켜야 하나요?"
    response = chat_gpt(user_message=user_message, system_message=system_message)
    print(response.choices[0].message.content)

def n_shot_prompting():
    # 0-shot
    response = chat_gpt(system_message = "당신은 유치원생입니다. 유치원생처럼 답변해주세요.",
                                   user_message = "오리")
    print(response.choices[0].message.content)
    
    # 1-shot
    messages = [
        OpenAIMessage(role="system", content="당신은 유치원생입니다. 유치원생처럼 답변해주세요."),
        OpenAIMessage(role="user", content="참새"),
        OpenAIMessage(role="assistant", content="짹짹"),
        OpenAIMessage(role="user", content="오리"),
    ]
    response = chat_gpt(messages=messages)
    print(response.choices[0].message.content)
    
    # 1-shot - 뱀
    messages = [
        OpenAIMessage(role="system", content="당신은 유치원생입니다. 유치원생처럼 답변해주세요."),
        OpenAIMessage(role="user", content="참새"),
        OpenAIMessage(role="assistant", content="짹짹"),
        OpenAIMessage(role="user", content="뱀"),
    ]
    response = chat_gpt(messages=messages)
    print(response.choices[0].message.content)
    
    # few-shot
    messages = [
        OpenAIMessage(role="system", content="당신은 유치원생입니다. 유치원생처럼 답변해주세요."),
        OpenAIMessage(role="user", content="참새"),
        OpenAIMessage(role="assistant", content="짹짹"),
        OpenAIMessage(role="user", content="말"),
        OpenAIMessage(role="assistant", content="히이잉"),
        OpenAIMessage(role="user", content="개구리"),
        OpenAIMessage(role="assistant", content="개굴개굴"),
        OpenAIMessage(role="user", content="뱀"),
    ]
    response = chat_gpt(messages=messages)
    print(response.choices[0].message.content)
    pass


def main():
    persona_1()
    

if __name__ == "__main__":
    main()
