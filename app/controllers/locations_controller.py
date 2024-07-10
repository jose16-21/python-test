from app.database.database import database
from app.file_models import locations
from app.validators.schemas import LocationCreate

async def create_location(location: LocationCreate):
    query = locations.insert().values(latitude=location.latitude, longitude=location.longitude)
    record_id = await database.execute(query)
    return {**location.dict(), "id": record_id}
