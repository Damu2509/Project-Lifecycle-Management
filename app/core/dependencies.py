from app.core.config import get_settings
from app.infra.llm.anthropic_client import AnthropicClient
from app.infra.llm.base import LLMClient
from app.infra.llm.ollama_client import OllamaClient
from app.infra.llm.openai_client import OpenAIClient


def get_llm_client() -> LLMClient:
    settings = get_settings()
    providers: dict[str, type[LLMClient]] = {
        "openai": OpenAIClient,
        "anthropic": AnthropicClient,
        "ollama": OllamaClient,
    }
    client_cls = providers.get(settings.llm_provider)
    if client_cls is None:
        raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
    return client_cls(settings)
