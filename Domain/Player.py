from typing import Optional
import uuid

from sqlmodel import Field, SQLModel

class Player(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    elo: int
    played_games: int