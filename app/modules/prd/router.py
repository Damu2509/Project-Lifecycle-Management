from fastapi import APIRouter

from app.modules.prd.schema import PRDRequest
from app.modules.prd.service import generate_prd

router = APIRouter(tags=["PRD"])


@router.post("/generate-prd")
async def create_prd(request: PRDRequest):
    return await generate_prd(request)
