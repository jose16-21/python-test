from fastapi import APIRouter
from app.controllers.category_controller import store
from app.validators.Category import CategoryCreate, Category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=Category)
async def add_category(category: CategoryCreate):
    return await store(category)
