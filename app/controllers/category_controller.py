from app.managers.category_manager import storeCategory, indexCategory
from app.validators.Category import CategoryCreate
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

from app.database.database import database
from sqlalchemy import select
from app.models.file_models import categories
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
async def store(category: CategoryCreate):
    return await storeCategory(category)


async def index(category: CategoryCreate):
    items = database.query(Item).all()
    return items
