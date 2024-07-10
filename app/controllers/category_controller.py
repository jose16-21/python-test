from app.managers.category_manager import store_category
from app.validators.schemas import CategoryCreate
async def store(category: CategoryCreate):
    print(category)
    return await store_category(category)