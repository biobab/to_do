# from typing import Optional #workswith ex.: age: int|None
from sqlmodel import Field, SQLModel, create_engine, Session, select
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
engine = create_engine(url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_item(new_item):
    item = Items(name=new_item)
    with Session(engine) as session:
        session.add(item)
        session.commit()
    # session.close() -> a with session miatt nem kell


def select_item(x):
    with Session(engine) as session:
        statement = select(Items).where(Items.id == x)
        result = session.exec(statement)
        item = result.one()
        print(item)


if __name__ == "__main__":
    create_db_and_tables()
    # create_item("-.-")
    select_item(1)
