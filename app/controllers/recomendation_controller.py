from app.managers.recomendation_manager import storeRecommendation
from app.validators.Recommendation import RecommendationCreate


async def store(recommendation: RecommendationCreate):
    return await storeRecommendation(recommendation)