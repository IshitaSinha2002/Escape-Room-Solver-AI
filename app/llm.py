from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field


load_dotenv()


class EscapeRoomDecision(BaseModel):
    next_action: str = Field(
        description="The next action the solver should take."
    )

    new_clue: str = Field(
        description="A new clue discovered from the current reasoning. "
                    "Return an empty string if there is no new clue."
    )

    observation: str = Field(
        description="What the solver has learned from the current situation."
    )

    is_solved: bool = Field(
        description="Whether the escape room has been solved."
    )

    solution: str = Field(
        description="The final solution if the room is solved. "
                    "Otherwise return an empty string."
    )


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

structured_llm = llm.with_structured_output(EscapeRoomDecision)