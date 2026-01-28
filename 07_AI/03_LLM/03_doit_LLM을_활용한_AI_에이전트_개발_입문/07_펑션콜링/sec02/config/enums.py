from enum import Enum

class OpenAIMessageRole(str, Enum):
    system      :str = "system"
    user        :str = "user"
    assistant   :str = "assistant"