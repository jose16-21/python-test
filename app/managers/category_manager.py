from app.validators.schemas import CategoryCreate
from app.repositories.category_repository import store
async def store_category(category: CategoryCreate):
    record_id = await store(category)
    return {**category.dict(), "id": record_id}
