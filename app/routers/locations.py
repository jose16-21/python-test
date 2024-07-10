from fastapi import APIRouter, HTTPException
from typing import List
from ..crud import create_location
from ..schemas import LocationCreate, Location

router = APIRouter(prefix="/locations", tags=["locations"])

@router.post("/", response_model=Location)
async def add_location(location: LocationCreate):
    return await create_location(location)
