from dataclasses import dataclass

@dataclass
class OpenAIMessage:
    role:str
    content:str