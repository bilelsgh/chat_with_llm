from abc import ABC, abstractmethod
from enum import Enum

from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate


class LLMClient(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = None
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", input_key="input", return_messages=True
        )

    @abstractmethod
    def ask(self, prompt: str, context: str = "") -> str:
        raise NotImplementedError

    def _init_conversation_context(self, prompt_instruction: str):
        """
        Configuration of every component needed to start the conversation.

        :param prompt_instruction: Custom prompt instruction for the conversation
        """

        if not prompt_instruction:
            prompt_template = """
            Here is the history of the conversation:
            {chat_history}

            User: {input}
            Assistant:
            """
        else:
            prompt_template = prompt_instruction
        input_variables = ["input", "chat_history"]

        prompt = PromptTemplate(
            template=prompt_template, input_variables=input_variables
        )

        self.conversation_chain = ConversationChain(
            llm=self.client, memory=self.memory, prompt=prompt, verbose=True
        )


class AvailableModels(Enum):
    DEEPSEEK_R1 = ("DEEPSEEK", "deepseek-chat")
    MISTRAL_LARGE = ("MISTRAL", "mistral-large-latest")

    def __init__(self, model_family: str, name: str):
        self._model_family = model_family
        self._name = name

    @property
    def model_family(self):
        return self._model_family

    @property
    def name(self):
        return self._name


available_models = {
    "deepseek-r1": AvailableModels.DEEPSEEK_R1,
    "mistral-large": AvailableModels.MISTRAL_LARGE,
}
