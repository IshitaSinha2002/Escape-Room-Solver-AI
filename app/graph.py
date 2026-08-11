from langgraph.graph import StateGraph, START, END

from app.state import EscapeRoomState
from app.nodes import analyze_room

def build_graph():
    graph = StateGraph(EscapeRoomState)

    graph.add_node("analyze_room", analyze_room)

    graph.add_edge(START, "analyze_room")
    graph.add_edge("analyze_room", END)

    return graph.compile()