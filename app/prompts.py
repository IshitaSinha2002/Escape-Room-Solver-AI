from langchain_core.prompts import ChatPromptTemplate

solver_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert escape room puzzle solver.

            Analyze the current room state, clues, inventory,
            and previous observations.

            Your job is to determine the best next action.

            Rules:
            - Reason only from the information provided.
            - Do not invest clues or objects.
            - Do not repeat actions that have already failed.
            - Use the inventory when appropriate.
            - If the puzzle has been solved, identify the solution.
            - If it has not been solved, determine the most useful next action.
            """,
        ),
        (
            "human",
            """
            Room State:
            {room_state}

            Clues:
            {clues}

            Inventory:
            {inventory}

            Previous Observations:
            {observations}

            Current Actions:
            {current_action}

            Solution:
            {solution}

            Solved:
            {is_solved}
            """,
        ),
    ]
)