from fastapi import APIRouter, HTTPException
from typing import List
from ..crud import get_recommendations
from ..schemas import LocationCategoryReviewed

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

@router.get("/", response_model=List[LocationCategoryReviewed])
async def recommend():
    return await get_recommendations()
