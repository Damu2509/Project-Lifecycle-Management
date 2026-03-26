import time
from functools import wraps
from typing import Any, Callable, Coroutine

from app.core.logger import get_logger

logger = get_logger(__name__)


def async_timer(func: Callable[..., Coroutine[Any, Any, Any]]):
    """Decorator that logs the wall-clock time of an async function."""

    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info("%s completed in %.2fs", func.__qualname__, elapsed)
        return result

    return wrapper
