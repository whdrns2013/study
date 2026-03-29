from core.streamlit_chat import streamlit_chat
from config.config import config
from test.terminal_chat import terminal_chat

STREAM=True

def main():
    if config["setting"]["mode.terminal"] == "1":
        terminal_chat(stream=STREAM)
    else:
        streamlit_chat(stream=STREAM)

if __name__ == "__main__":
    main()
