from typing import Protocol


class LLMProvider(Protocol):
    def invoke(self, message: str) -> str:
        ...