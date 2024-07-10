from app.database.database import database
from app.file_models import locations
from app.validators.schemas import LocationCreate


async def store(location: LocationCreate):
    query = locations.insert().values(latitude=location.latitude, longitude=location.longitude)
    return await database.execute(query)
