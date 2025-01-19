"""
MistralAI Client
"""

from mistralai import Mistral

from clients.base import LLMClient


class MistralClient(LLMClient):
    def __init__(self, key: str, model_name: str = "mistralai/Mistral-7B-v0.1"):
        super().__init__(model_name)
        self.client = Mistral(api_key=key)

    def ask(self, prompt: str, content_only: bool = True) -> str:
        """
        Ask something to the model

        :param prompt: Prompt for the model
        :param content_only: If True, return only the content of the response. Else return the entire response - default True
        :return response: Model answer
        """

        response = self.client.chat.complete(
            model=self.model_name, messages=[{"role": "user", "content": prompt}]
        )

        if content_only:
            return response.choices[0].message.content

        return response

    def ask_with_context(self, prompt: str, context: str) -> str:
        """
        Ask something to the model

        :param prompt: Prompt for the model
        :param context: Context for the model
        :return: Model answer
        """

        return self.ask(f"{prompt}" f"\n{context}")
