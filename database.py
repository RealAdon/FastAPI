from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the Database Urls
DATABASE_URL = 'sqlite:///./database.db'

# Create the engine
engine = create_engine(DATABASE_URL,connect_args={'check_same_thread': False})

# Define a Session as local
SessionLocal = sessionmaker(bind=engine)

# Define the Base
Base = declarative_base()

# Function to get Database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()