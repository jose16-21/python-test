from fastapi import APIRouter, HTTPException
from typing import List
from ..crud import create_category
from ..schemas import CategoryCreate, Category

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=Category)
async def add_category(category: CategoryCreate):
    return await create_category(category)
