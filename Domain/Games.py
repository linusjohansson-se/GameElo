
from datetime import datetime
from typing import Optional
import uuid
from sqlmodel import Field, SQLModel


class Games(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    winner_id: uuid.UUID
    loser_id: uuid.UUID
    date: datetime