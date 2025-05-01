from sqlmodel import create_engine
from models import SQLModel

# create session
engine = create_engine('sqlite:///database.db') # Use your database URL
SQLModel.metadata.create_all(engine) # Creates tables if they don't exist
