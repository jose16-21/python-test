from app.database.database import database
from app.models.file_models import reviews
from app.validators.Recommendation import RecommendationCreate


async def store(recommendation: RecommendationCreate):
    query = reviews.insert().values(
        location_id=recommendation.location_id,
        category_id=recommendation.category_id,
        score=recommendation.score,
        recommended_at= recommendation.recommended_at)
    return await database.execute(query)
