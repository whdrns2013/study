from langgraph.graph import StateGraph, START, END
from graph.state import AppState
from graph import nodes

class UpDownGameGraph:
    
    @staticmethod
    def get_state():
        return AppState
    
    @staticmethod
    def build():
        graph = StateGraph(AppState)
        graph.add_node("generate", nodes.generate_node)
        graph.add_node("terminate", nodes.terminate_node)

        graph.add_conditional_edges(START, nodes.input_routing_function, {True:"terminate", False:"generate"})
        graph.add_conditional_edges("generate", nodes.routing_function, {True:"terminate", False:"generate"})
        graph.add_edge("terminate", END)

        app = graph.compile()
        return app, graph