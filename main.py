from app.graph import build_graph

def main():
    graph = build_graph()

    initial_state = {
        "room_state": """
        You are trapped inside an old study.
        The main door is locked.
        There is a clock stopped at 3:15.
        A wooden drawer has a 3-digit keypad.
        """,

        "clues": [
            "The clock is stopped at 3:15",
            "The drawer requires a 3-digit code"
        ],

        "inventory": [
            "small brass key"
        ],

        "observations": [],

        "current_action": "",

        "action_result": "",

        "solution": "",

        "is_solved": False
    }

    result = graph.invoke(initial_state)

    print("\n===== ESCAPE ROOM SOLVER =====\n")

    print("Next Action:")
    print(result["current_action"])

    print("\nAction Result:")
    print(result["action_result"])

    print("\nObservation:")
    print(result["observations"][-1])


if __name__ == "__main__":
    main()