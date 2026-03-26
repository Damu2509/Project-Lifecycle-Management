import httpx

from app.core.config import Settings
from app.core.exceptions import LLMConnectionError, LLMError
from app.core.logger import get_logger
from app.infra.llm.base import LLMClient

logger = get_logger(__name__)


class OllamaClient(LLMClient):
    """Client for Ollama-compatible /api/generate endpoints (local or tunneled via ngrok)."""

    def __init__(self, settings: Settings) -> None:
        self._base_url = settings.llm_base_url.rstrip("/")
        self._model = settings.model_name
        self._client = httpx.AsyncClient(timeout=120.0)

    async def generate(self, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "ngrok-skip-browser-warning": "true",
        }
        payload = {
            "model": self._model,
            "prompt": prompt,
            "stream": False,
        }

        try:
            response = await self._client.post(
                self._base_url, headers=headers, json=payload
            )
            response.raise_for_status()
            data = response.json()
            return data["response"]
        except httpx.ConnectError as exc:
            logger.error("Ollama connection failed: %s", exc)
            raise LLMConnectionError(detail=str(exc))
        except httpx.HTTPStatusError as exc:
            logger.error(
                "Ollama HTTP error %s: %s",
                exc.response.status_code,
                exc.response.text,
            )
            raise LLMError(detail=f"Ollama returned {exc.response.status_code}")
        except KeyError:
            logger.error("Unexpected Ollama response format: %s", data)
            raise LLMError(detail="Ollama response missing 'response' field")
        except Exception as exc:
            logger.error("Unexpected Ollama error: %s", exc)
            raise LLMError(detail=str(exc))

    async def close(self) -> None:
        await self._client.aclose()
