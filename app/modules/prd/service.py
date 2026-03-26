import httpx
from app.core.config import get_settings
from app.modules.prd.schema import PRDRequest

from app.shared.constants import  OPEN_SOURCE_LLM_HEADERS


async def generate_prd(request: PRDRequest) -> dict:
    settings = get_settings()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=settings.llm_base_url,
            json={
                "model": settings.model_name,
                "prompt": request.idea,
                "stream": False,
            },
            headers={
               OPEN_SOURCE_LLM_HEADERS
            },
            timeout=60.0,
        )
        response.raise_for_status()

    return response.json().get("response")
