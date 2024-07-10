from app.validators.schemas import LocationCreate
from app.repositories.location_repository import store

async def storeLocation(location: LocationCreate):
    record_id = await store(location)
    return {**location.dict(), "id": record_id}