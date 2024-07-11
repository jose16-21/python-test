from app.managers.category_manager import storeCategory
from app.validators.Category import CategoryCreate


async def store(category: CategoryCreate):
    return await storeCategory(category)
