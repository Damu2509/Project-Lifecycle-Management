import httpx

from app.core.config import Settings
from app.core.exceptions import LLMConnectionError, LLMError
from app.core.logger import get_logger
from app.infra.llm.base import LLMClient

logger = get_logger(__name__)

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"


class AnthropicClient(LLMClient):
    def __init__(self, settings: Settings) -> None:
        self._api_key = settings.llm_api_key
        self._model = settings.model_name or "claude-sonnet-4-20250514"
        self._client = httpx.AsyncClient(timeout=60.0)

    async def generate(self, prompt: str) -> str:
        headers = {
            "x-api-key": self._api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self._model,
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}],
        }

        try:
            response = await self._client.post(
                ANTHROPIC_API_URL, headers=headers, json=payload
            )
            response.raise_for_status()
            data = response.json()
            return data["content"][0]["text"]
        except httpx.ConnectError as exc:
            logger.error("Anthropic connection failed: %s", exc)
            raise LLMConnectionError(detail=str(exc))
        except httpx.HTTPStatusError as exc:
            logger.error(
                "Anthropic HTTP error %s: %s",
                exc.response.status_code,
                exc.response.text,
            )
            raise LLMError(detail=f"Anthropic returned {exc.response.status_code}")
        except Exception as exc:
            logger.error("Unexpected Anthropic error: %s", exc)
            raise LLMError(detail=str(exc))

    async def close(self) -> None:
        await self._client.aclose()
