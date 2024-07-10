from fastapi import FastAPI
from app.database.database import database, engine, metadata
from app.routers import locations, categories, recommendations

metadata.create_all(engine)

app = FastAPI()

app.include_router(locations.router)
app.include_router(categories.router)
app.include_router(recommendations.router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
