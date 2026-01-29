from core.streamlit_chat import streamlit_chat
from config.config import config
from test.terminal_chat import terminal_chat

def main():
    if config["setting"]["mode.terminal"] == "1":
        terminal_chat()
    else:
        streamlit_chat()

if __name__ == "__main__":
    main()
