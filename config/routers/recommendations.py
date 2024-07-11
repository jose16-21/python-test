from fastapi import APIRouter
from typing import List
from app.controllers.recomendation_controller import store
from app.controllers.reviewed_controller import get_recommendations
from app.validators.schemas import LocationCategoryReviewed
from app.validators.Recommendation import Recommendation, RecommendationCreate
router = APIRouter(prefix="/recommendations", tags=["recommendations"])


@router.get("/", response_model=List[LocationCategoryReviewed])
async def recommend():
    return await get_recommendations()


@router.post("/", response_model=Recommendation)
async def recommend(recommendation: RecommendationCreate):
    return await store(recommendation)
