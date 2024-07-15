from app.database.database import database
from sqlalchemy import select
from app.models.file_models import categories
from app.validators.Category import CategoryCreate


async def store(category: CategoryCreate):
    query = categories.insert().values(name=category.name, description=category.description)
    return await database.execute(query)


async def index(category: CategoryCreate):
    select_stmt = select([categories.c.name, categories.c.description])
    result = database.fetch_all(select_stmt)

    for row in result:
        print(row)
