import json

from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from controllers.storageQuantity import get_storage_quantity, create_storage_quantity
from schemas import schemas
from models.database import get_db

router = APIRouter()


@router.post('/')
def add_storage_quantity(data: List[schemas.StorageQuantityCreate], db: Session = Depends(get_db)):
    for storage_quantity in data:
        create_storage_quantity(db, storage_quantity)

    return {"a": data}


@router.get('/', response_model=List[schemas.StorageQuantity])
def read_storages_quantity(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    storage_quantity = get_storage_quantity(db, skip, limit)

    if storage_quantity is None:
        raise HTTPException(status_code=404, detail="Storage quantity not found")

    return storage_quantity
