from sqlalchemy.orm import Session
from models import models
from schemas import schemas


def get_storage_quantity(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.StorageQuantity).offset(skip).limit(limit).all()


def create_storage_quantity(db: Session, storage_quantity: schemas.StorageQuantityCreate):
    db_storage_quantity = models.StorageQuantity(**storage_quantity.model_dump())

    if db_storage_quantity.product_id == 7:
        db_storage_quantity.count = db_storage_quantity.count * 20
    elif db_storage_quantity.product_id == 8 or db_storage_quantity.product_id == 9:
        db_storage_quantity.count = db_storage_quantity.count * 50

    db.add(db_storage_quantity)
    db.commit()
    db.refresh(db_storage_quantity)
    return db_storage_quantity
