import os
import streamlit.components.v1 as components

_component_func = components.declare_component(
    "stopwatch",
    path=os.path.join(os.path.dirname(__file__), "frontend"),
)

def stopwatch(key=None):
    return _component_func(key=key, default=None)