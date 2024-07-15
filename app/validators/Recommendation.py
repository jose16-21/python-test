from pydantic import BaseModel
from datetime import datetime


class RecommendationBase(BaseModel):
    location_id: int
    category_id: int
    score: float


class RecommendationCreate(RecommendationBase):
    pass


class Recommendation(RecommendationBase):
    id: int

    class Config:
        orm_mode = True