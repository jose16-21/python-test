from app.database.database import database
from app.file_models import categories
from app.validators.schemas import CategoryCreate


async def store(category: CategoryCreate):
    query = categories.insert().values(name=category.name)
    return await database.execute(query)
