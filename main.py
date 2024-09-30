from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from db import models
from db.engine import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/category", response_model=list[schemas.Category])
def read_category(db: Session = Depends(get_db)):
    return crud.get_all_categories(db)
