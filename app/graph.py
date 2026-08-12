from langgraph.graph import StateGraph, START, END

from app.state import EscapeRoomState
from app.nodes import analyze_room, execute_action

def build_graph():
    graph = StateGraph(EscapeRoomState)

    graph.add_node("analyze_room", analyze_room)
    graph.add_node("execute_action", execute_action)

    graph.add_edge(START, "analyze_room")
    graph.add_edge("analyze_room", "execute_action")
    graph.add_edge("execute_action", END)

    return graph.compile()