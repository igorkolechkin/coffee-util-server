from sqlalchemy.orm import Session
from models import models
from schemas import schemas


def get_storage(db: Session, storage_id: int):
    return db.query(models.Storage).filter(models.Storage.id == storage_id).first()


def get_storages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Storage).offset(skip).limit(limit).all()


def create_storage(db: Session, storage: schemas.StorageCreate):
    db_storage = models.Storage(**storage.model_dump())
    db.add(db_storage)
    db.commit()
    db.refresh(db_storage)
    return db_storage
