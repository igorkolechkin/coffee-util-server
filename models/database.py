from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_CONNECTION_URL

engine = create_engine(DB_CONNECTION_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
