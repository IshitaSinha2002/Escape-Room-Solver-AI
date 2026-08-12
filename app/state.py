from typing import TypedDict, List

class EscapeRoomState(TypedDict):
    room_state: str
    clues: List[str]
    inventory: List[str]
    observations: List[str]
    current_action: str
    action_result: str
    solution: str
    is_solved: bool