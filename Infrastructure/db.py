from sqlmodel import SQLModel, create_engine
from Domain.Player import Player
from Domain.Games import Games

engine = create_engine("sqlite:///db.sqlite3", echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)