from altas.providers.base import LLMProvider


class ChatApplication:

    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def chat(self, message: str) -> str:
        return self.provider.invoke(message)