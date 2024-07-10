from fastapi import APIRouter
from app.controllers.locations_controller import store
from app.validators.schemas import LocationCreate, Location

router = APIRouter(prefix="/locations", tags=["locations"])


@router.post("/", response_model=Location)
async def add_location(location: LocationCreate):
    return await store(location)
