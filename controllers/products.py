from sqlalchemy.orm import Session
from sqlalchemy import text
from models import models


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_products(db: Session, storage_id: int = 0):
    if storage_id != 0:
        return (db.query(models.Product)
                .filter(text(':storage_id = ANY(to_storages)').params(storage_id=storage_id))
                .all())
    else:
        return db.query(models.Product).all()
