from langgraph.graph import StateGraph, START, END

from app.state import EscapeRoomState
from app.nodes import (analyze_room, execute_action, check_solved)

def route_after_check(state: EscapeRoomState):
    if state["is_solved"]:
        return "end"
    return "continue"

def build_graph():
    graph = StateGraph(EscapeRoomState)

    graph.add_node("analyze_room", analyze_room)
    graph.add_node("execute_action", execute_action)
    graph.add_node("check_solved", check_solved)

    graph.add_edge(START, "analyze_room")
    graph.add_edge("analyze_room", "execute_action")
    graph.add_edge("execute_action", "check_solved")
    graph.add_conditional_edges("check_solved", route_after_check, {"continue": "analyze_room","end": END})

    return graph.compile()