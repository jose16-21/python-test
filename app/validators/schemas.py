from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LocationBase(BaseModel):
    latitude: float
    longitude: float

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class LocationCategoryReviewedBase(BaseModel):
    location_id: int
    category_id: int

class LocationCategoryReviewedCreate(LocationCategoryReviewedBase):
    pass

class LocationCategoryReviewed(LocationCategoryReviewedBase):
    id: int
    reviewed_at: datetime

    class Config:
        orm_mode = True
