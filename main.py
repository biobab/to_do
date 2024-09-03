# from typing import Optional #workswith ex.: age: int|None
from sqlmodel import Field, SQLModel
from datetime import datetime, UTC


class Items(SQLModel, table=True):
    __tablename__ = "items"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    time_added: datetime = datetime.now(UTC)
    completed: bool = False
