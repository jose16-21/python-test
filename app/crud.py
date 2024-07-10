from sqlalchemy import select
from .database import database
from .models import locations, categories, location_category_reviewed
from .schemas import LocationCreate, CategoryCreate, LocationCategoryReviewedCreate

async def create_location(location: LocationCreate):
    query = locations.insert().values(latitude=location.latitude, longitude=location.longitude)
    record_id = await database.execute(query)
    return {**location.dict(), "id": record_id}

async def create_category(category: CategoryCreate):
    query = categories.insert().values(name=category.name)
    record_id = await database.execute(query)
    return {**category.dict(), "id": record_id}

async def create_location_category_reviewed(review: LocationCategoryReviewedCreate):
    query = location_category_reviewed.insert().values(
        location_id=review.location_id,
        category_id=review.category_id
    )
    record_id = await database.execute(query)
    return {**review.dict(), "id": record_id}

async def get_recommendations():
    query = select([
        location_category_reviewed.c.location_id,
        location_category_reviewed.c.category_id
    ]).order_by(location_category_reviewed.c.reviewed_at)
    results = await database.fetch_all(query)
    return results
