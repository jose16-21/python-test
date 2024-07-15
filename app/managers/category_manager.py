from app.validators.Category import CategoryCreate
from app.repositories.category_repository import store, index


async def storeCategory(category: CategoryCreate):
    record_id = await store(category)
    return {**category.dict(), "id": record_id}


async def indexCategory(category: CategoryCreate):
    print(1111111111111111)
    query = await index(category)
    print(query)
    return query
