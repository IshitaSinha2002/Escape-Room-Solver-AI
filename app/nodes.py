from app.state import EscapeRoomState
from app.llm import llm
from app.prompts import solver_prompt

def analyze_room(state: EscapeRoomState):
    prompt = solver_prompt.invoke(
        {
            "room_state": state["room_state"],
            "clues": state["clues"],
            "inventory": state["inventory"],
            "observations": state["observations"],
            "current_action": state["current_actions"],
            "solution": state["solution"],
            "is_solved": state["is_solved"],
        }
    )

    response = llm.invoke(prompt)

    return {
        "observations": state["observations"] + [response.content],
        "current_action": response.content
    }