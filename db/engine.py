from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace with your own PostgreSQL instance
# Use %40 instead of @ symbol to avoid conflicts
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Vfwzkrf17%40@localhost/challenge"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
