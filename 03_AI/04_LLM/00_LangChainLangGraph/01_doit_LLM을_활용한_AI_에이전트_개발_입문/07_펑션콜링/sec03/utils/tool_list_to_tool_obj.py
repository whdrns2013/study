from dataclasses import dataclass, asdict
from collections import defaultdict

@dataclass
class OpenAIFunction:
    arguments   :str|None=""
    name        :str|None=None

@dataclass
class ToolObject:
    id          :str|None=None
    function    :OpenAIFunction|None=None
    type        :str|None=None

def tool_list_to_tool_obj(tools:list):
    tool_map = defaultdict(lambda: ToolObject(function=OpenAIFunction()))
    
    for tool_call in tools:
        to = tool_map[tool_call.index]
        
        # tool call ID
        if tool_call.id is not None:
            to.id = tool_call.id
        
        # function name
        if tool_call.function.name is not None:
            to.function.name = tool_call.function.name
    
        # arguments
        to.function.arguments += tool_call.function.arguments
        
        # tool call type
        if tool_call.type is not None:
            to.type = tool_call.type
    
    return {"tool_calls" : [asdict(to) for to in tool_map.values()]}