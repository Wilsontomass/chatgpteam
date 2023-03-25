# This conversation type should exclude the system message _and_ the first user message (containing information specific to each AI)
from typing import Dict, List


MODEL = "gpt-4"
Conversation = List[Dict[str, str]]
PROJECT = "a command line inventory management app"


def print_message(message: Dict[str, str]):
    print(f"{message['role']}: {message['content']}")
    print()
