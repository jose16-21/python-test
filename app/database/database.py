from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "mysql+pymysql://user:password@localhost/map_my_world"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)