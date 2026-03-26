import httpx

from app.core.config import Settings
from app.core.exceptions import LLMConnectionError, LLMError
from app.core.logger import get_logger
from app.infra.llm.base import LLMClient

logger = get_logger(__name__)


class OpenAIClient(LLMClient):
    def __init__(self, settings: Settings) -> None:
        self._api_key = settings.llm_api_key
        self._base_url = settings.llm_base_url.rstrip("/")
        self._model = settings.model_name
        self._client = httpx.AsyncClient(timeout=60.0)

    async def generate(self, prompt: str) -> str:
        url = f"{self._base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self._model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }

        try:
            response = await self._client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except httpx.ConnectError as exc:
            logger.error("OpenAI connection failed: %s", exc)
            raise LLMConnectionError(detail=str(exc))
        except httpx.HTTPStatusError as exc:
            logger.error("OpenAI HTTP error %s: %s", exc.response.status_code, exc.response.text)
            raise LLMError(detail=f"OpenAI returned {exc.response.status_code}")
        except Exception as exc:
            logger.error("Unexpected OpenAI error: %s", exc)
            raise LLMError(detail=str(exc))

    async def close(self) -> None:
        await self._client.aclose()
