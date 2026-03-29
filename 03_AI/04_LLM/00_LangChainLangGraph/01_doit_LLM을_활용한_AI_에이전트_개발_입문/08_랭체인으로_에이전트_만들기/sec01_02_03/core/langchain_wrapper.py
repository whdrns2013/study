from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
from core.openai_model import get_model
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

class LangChainWrapper:

    message_type_dict = {
        "system" : SystemMessage,
        "assistant": AIMessage,
        "user": HumanMessage
    }

    def __init__(self, model_name:str|None=None, api_key:str|None=None):
        self.core_model = get_model(model=model_name, api_key=api_key)
    
    @staticmethod
    def get_session_history(self, session_id:str, store) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]
    
    @classmethod
    def get_with_message_history(cls, session_id,
                                 store,
                                 model_name:str|None=None, api_key:str|None=None):
        lcw = cls(model_name, api_key)
        session_id = session_id
        store = store
        with_message_history = RunnableWithMessageHistory(lcw.core_model,
                                                          lambda sid: cls.get_session_history(sid, store))
        return with_message_history
        