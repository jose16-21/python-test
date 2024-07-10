from app.managers.category_manager import storeCategory
from app.validators.schemas import CategoryCreate


async def store(category: CategoryCreate):
    return await storeCategory(category)
