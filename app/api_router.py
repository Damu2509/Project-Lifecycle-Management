from fastapi import APIRouter

from app.modules.health.router import router as health_router
from app.modules.prd.router import router as prd_router

router = APIRouter()

router.include_router(health_router)
router.include_router(prd_router)
