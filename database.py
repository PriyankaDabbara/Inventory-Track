from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
db_url="postgres Enter your db_url"
engine = create_engine(db_url)
session= sessionmaker(autocommit=False, autoflush=False, bind=engine)