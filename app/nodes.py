from app.state import EscapeRoomState
from app.llm import structured_llm
from app.prompts import solver_prompt


def analyze_room(state: EscapeRoomState):
    prompt = solver_prompt.invoke(
        {
            "room_state": state["room_state"],
            "clues": state["clues"],
            "inventory": state["inventory"],
            "observations": state["observations"],
            "current_action": state["current_action"],
            "solution": state["solution"],
            "is_solved": state["is_solved"],
        }
    )

    decision = structured_llm.invoke(prompt)

    new_clues = state["clues"].copy()

    if decision.new_clue:
        new_clues.append(decision.new_clue)

    new_observations = state["observations"].copy()
    new_observations.append(decision.observation)

    return {
        "clues": new_clues,
        "observations": new_observations,
        "current_action": decision.next_action,
        "is_solved": decision.is_solved,
        "solution": decision.solution
    }