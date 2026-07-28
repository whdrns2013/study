from core.config import config
from feature.openai_api import chat_gpt

def main():
    user_message = "안녕하세요. 반갑습니다."
    response = chat_gpt(user_message)
    print(response)
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
