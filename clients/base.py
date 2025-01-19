from abc import ABC, abstractmethod
from enum import Enum


class LLMClient(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = None

    @abstractmethod
    def ask(self, prompt: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def ask_with_context(self, prompt: str, context: str) -> str:
        raise NotImplementedError


class AvailableClients(Enum):
    MISTRAL = "mistral"


def get_client_from_input(user_input: str) -> AvailableClients:
    """
    Get LLM client from user input

    :param user_input: LLM Family
    :return: AvailableClients
    """

    try:
        return AvailableClients(user_input)
    except ValueError:
        raise ValueError(f"Invalid client: {user_input}")
