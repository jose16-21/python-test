from fastapi import APIRouter
from typing import List
from app.controllers.reviewed_controller import get_recommendations
from app.validators.schemas import LocationCategoryReviewed

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

@router.get("/", response_model=List[LocationCategoryReviewed])
async def recommend():
    return await get_recommendations()
