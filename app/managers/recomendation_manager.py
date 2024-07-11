from app.validators.Recommendation import RecommendationCreate
from app.repositories.recomendation_repository import store


async def storeRecommendation(recommendation: RecommendationCreate):
    record_id = await store(recommendation)
    return {**recommendation.dict(), "id": record_id}
