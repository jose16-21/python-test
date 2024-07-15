from sqlalchemy import select
from app.database.database import database
from app.models.file_models import reviews
from app.validators.schemas import LocationCategoryReviewedCreate


async def create_location_category_reviewed(review: LocationCategoryReviewedCreate):
    query = reviews.insert().values(
        location_id=review.location_id,
        category_id=review.category_id
    )
    record_id = await database.execute(query)
    return {**review.dict(), "id": record_id}


async def get_recommendations():
    query = select([
        reviews.c.location_id,
        reviews.c.category_id
    ]).order_by(reviews.c.reviewed_at)
    return await database.fetch_all(query)