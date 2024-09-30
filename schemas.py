from typing import List

from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    title: str
    points: List[str]


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True
