from fastapi import APIRouter
from typing import List
from app.controllers.category_controller import store, index
from app.validators.Category import CategoryCreate, Category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=Category)
async def add_category(category: CategoryCreate):
    return await store(category)


@router.get("/", response_model=Category)
async def get_categories(category: CategoryCreate):
    return await index(category)
