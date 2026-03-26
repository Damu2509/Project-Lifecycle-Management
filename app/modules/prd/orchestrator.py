import asyncio

from app.core.logger import get_logger
from app.infra.llm.base import LLMClient
from app.modules.prd.prompts import PRD_PROMPT, SUGGESTION_PROMPT, VALIDATION_PROMPT
from app.shared.utils import async_timer

logger = get_logger(__name__)


@async_timer
async def run(idea: str, llm: LLMClient) -> dict[str, str]:
    """Run all three LLM calls concurrently and return combined results."""

    # logger.info("Starting PRD orchestration for idea: %.80s…", idea)

    # validation_coro = llm.generate(VALIDATION_PROMPT.format(idea=idea))
    # prd_coro = llm.generate(PRD_PROMPT.format(idea=idea))
    # suggestion_coro = llm.generate(SUGGESTION_PROMPT.format(idea=idea))

    # validation, prd, suggestion = await asyncio.gather(
    #     validation_coro, prd_coro, suggestion_coro
    # )
    result = await asyncio.gather(
        validation_coro, prd_coro, suggestion_coro
    )
    return result

    # return {
    #     "validation": validation,
    #     "prd": prd,
    #     "suggestion": suggestion,
    # }
