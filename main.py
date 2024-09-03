# from typing import Optional #workswith ex.: age: int|None
from sqlmodel import Field, SQLModel, create_engine, Session
from datetime import datetime, UTC
import dotenv
import os


class Items(SQLModel, table=True):
    __tablename__ = "items"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    time_added: datetime = datetime.now(UTC)
    completed: bool = False


dotenv.load_dotenv()
url = os.environ["DATABASE_URL"]
engine = create_engine(url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_item(name):
    item = Items(name=name)
    session = Session(engine)
    with session:
        session.add(item)
        session.commit()
    # session.close() -> a with session miatt nem kell


if __name__ == "__main__":
    create_db_and_tables()
    create_item(" ,@/'' ")
