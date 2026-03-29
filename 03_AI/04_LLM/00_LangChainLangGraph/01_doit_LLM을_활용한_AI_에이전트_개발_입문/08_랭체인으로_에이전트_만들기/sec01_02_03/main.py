from core import langchain_streamlit
from core import langchain_streamlit_tool_0
from core import langchain_streamlit_tool
from config.config import config

def main():
    langchain_streamlit_tool.streamlit_chat(config.getboolean("setting", "mode.stream"))


if __name__ == "__main__":
    main()
