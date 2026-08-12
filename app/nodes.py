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

def execute_action(state: EscapeRoomState):
    action = state["current_action"].lower()

    inventory = state["inventory"].copy()
    clues = state["clues"].copy()

    if "315" in action and "drawer" in action:
        action_result = (
            "The code 315 is correct. "
            "The wooden drawer opens. "
            "Inside the drawer, you find a silver key."
        )

        if "silver key" not in inventory:
            inventory.append("silver key")

        clues.append("The silver key may unlock the main door.")

    elif "silver key" in action and "door" in action:
        action_result = (
            "You use the silver key on the main door. "
            "The door unlocks."
        )

    else:
        action_result = (
            f"You attempt to perform the following action: {state['current_action']}. "
            "Nothing significant happens."
        )

    return {
        "inventory": inventory,
        "clues": clues,
        "action_result": action_result,
        "observations": state["observations"] + [action_result]
    }

def check_solved(state: EscapeRoomState):
    if "door unlocks" in state["action_result"].lower():
        return {
            "is_solved": True,
            "solution": "Use the silver key to unlock the main door."
        }

    return {
        "is_solved": False
    }