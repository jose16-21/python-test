from app.validators.Category import CategoryCreate
from app.repositories.category_repository import store


async def storeCategory(category: CategoryCreate):
    record_id = await store(category)
    return {**category.dict(), "id": record_id}
