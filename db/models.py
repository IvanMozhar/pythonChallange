from sqlalchemy import Column, Integer, String, ARRAY

from db.engine import Base


class DBCategory(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    points = Column(ARRAY(String), nullable=False)
