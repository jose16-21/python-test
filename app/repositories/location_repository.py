from app.database.database import database
from app.models.file_models import locations
from app.validators.Location import LocationCreate


async def store(location: LocationCreate):
    query = locations.insert().values(latitude=location.latitude, longitude=location.longitude)
    return await database.execute(query)
