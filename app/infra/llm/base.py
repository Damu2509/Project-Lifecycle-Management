from abc import ABC, abstractmethod


class LLMClient(ABC):
    """Abstract base class for all LLM provider clients."""

    @abstractmethod
    async def generate(self, prompt: str) -> str:
        """Send a prompt and return the generated text."""
        ...

    @abstractmethod
    async def close(self) -> None:
        """Release any underlying resources (HTTP connections, etc.)."""
        ...
