from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import TypedDict, Annotated, List
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict): #State is a class that inherits from TypedDict, State will act like a dictionary but with fixed keys and expected data types
    """
    Represents the structure of the state used in the graph.
    """
    messages: Annotated[list, add_messages] # messages is a key inside State dictionary and Annotated → A way to add extra metadata to a type hint.
