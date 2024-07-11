from pydantic import BaseModel
from typing import Optional
from datetime import datetime


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
