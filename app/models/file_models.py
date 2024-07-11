from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, DateTime, func
from app.database.database import metadata

locations = Table(
    "locations",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("latitude", Float, nullable=False),
    Column("longitude", Float, nullable=False),
)

categories = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(255), nullable=False, unique=True),
)

location_category_reviewed = Table(
    "location_category_reviewed",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("location_id", Integer, ForeignKey("locations.id"), nullable=False),
    Column("category_id", Integer, ForeignKey("categories.id"), nullable=False),
    Column("reviewed_at", DateTime, default=func.now(), nullable=False),
)

recommendations = Table(
    "recommendations",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("location_id", Integer, ForeignKey("locations.id"), nullable=False),
    Column("category_id", Integer, ForeignKey("categories.id"), nullable=False),
    Column("score", Float, nullable=False),
    Column("recommended_at", DateTime, default=func.now(), nullable=False),
)