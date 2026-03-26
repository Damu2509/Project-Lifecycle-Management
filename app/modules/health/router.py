from fastapi import APIRouter

from app.modules.health.service import check_health

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    return await check_health()
