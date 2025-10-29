import reflex as rx
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///reflex.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Initializes the database and creates tables if they don't exist."""
    from app.models.db_models import Base

    Base.metadata.create_all(bind=engine)


@contextmanager
def get_db():
    """Provides a database session within a context."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()