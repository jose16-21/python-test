from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, DateTime, func
from app.database.database import metadata
from sqlalchemy.orm import validates
from sqlalchemy.sql import func

locations = Table(
    "locations",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(255), unique=True, nullable=False),
    Column("description", String(255), nullable=False),
    Column("latitude", Float, nullable=False),
    Column("longitude", Float, nullable=False),
    Column("created_at", DateTime, nullable=False, default=func.now())
)

categories = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(255), nullable=False, unique=True),
    Column("description", String(255), nullable=False),
    Column("created_at", DateTime, nullable=False, default=func.now()),
)

location_category = Table(
    "location_category",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("location_id", Integer, ForeignKey("locations.id"), nullable=False),
    Column("category_id", Integer, ForeignKey("categories.id"), nullable=False),
    Column("created_at", DateTime, nullable=False, default=func.now()),
)

reviews = Table(
    "reviews",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("location_id", Integer, ForeignKey("locations.id"), nullable=False),
    Column("rating", Float, nullable=False),
    Column("comment", String(255), nullable=False),
    Column("created_at", DateTime, nullable=False, default=func.now())
)


# Validation to ensure rating is between 1 and 5
class ReviewValidator:
    @validates('rating')
    def validate_rating(self, key, value):
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5")
        return value
