from app.managers.location_manager import storeLocation
from app.validators.schemas import LocationCreate


async def store(location: LocationCreate):
    return await storeLocation(location)
