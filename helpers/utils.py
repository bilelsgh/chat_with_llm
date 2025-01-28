"""
Utils functions for the whole project
"""
from clients.deep_seek import DeepSeekClient
from clients.llmclient import AvailableModels, LLMClient, available_models
from clients.mistral import MistralClient


def get_llm_client(model: AvailableModels, key: str) -> LLMClient:
    """
    Get the LLM client to start chatting

    :param key: API key
    :param model: Desired model
    :return:
    """

    clients = {
        "DEEPSEEK": DeepSeekClient,
        "MISTRAL": MistralClient,
    }

    args_ = {"model_name": model.name, "key": key}

    return clients[model.model_family](**args_)


def get_model_type_from_input(user_input: str) -> AvailableModels:
    """
    Get LLM client from user input

    :param user_input: LLM Family
    :return: AvailableClients
    """

    try:
        return available_models[user_input]
    except KeyError:
        raise ValueError(f"Invalid client: {user_input}")
