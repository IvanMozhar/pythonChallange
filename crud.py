from sqlalchemy.orm import Session
from db import models
import schemas


def get_all_categories(db: Session):
    return db.query(models.DBCategory).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.DBCategory(
        name=category.title,
        points=category.points
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
