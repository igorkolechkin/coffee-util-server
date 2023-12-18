from sqlalchemy import func
from sqlalchemy.orm import Session, load_only
from models import models
from schemas import schemas
from datetime import datetime


def get_storages_quantity(db: Session, storage_id, month):
    storageQuantity = models.StorageQuantity

    query = (db.query(storageQuantity)
             .options(
                load_only(
                    storageQuantity.product_id,
                    storageQuantity.price,
                    storageQuantity.count,
                    storageQuantity.date
                )
            )
            .filter(storageQuantity.storage_id == storage_id))

    if month != 'all':
        query = query.filter(func.substring(storageQuantity.date, 6, 2) == month)

    return query.all()


def create_storage_quantity(db: Session, storage_quantity: schemas.StorageQuantityCreate):
    db_storage_quantity = models.StorageQuantity(**storage_quantity.model_dump())

    if db_storage_quantity.product_id == 10:
        db_storage_quantity.count = db_storage_quantity.count * 15
    elif db_storage_quantity.product_id == 11 or db_storage_quantity.product_id == 12:
        db_storage_quantity.count = db_storage_quantity.count * 50

    db.add(db_storage_quantity)
    db.commit()
    db.refresh(db_storage_quantity)
    return db_storage_quantity
