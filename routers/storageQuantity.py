from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from controllers.storageQuantity import get_storages_quantity, create_storage_quantity
from schemas import schemas
from models.database import get_db

router = APIRouter()


@router.post('/')
def add_storage_quantity(data: List[schemas.StorageQuantityCreate], db: Session = Depends(get_db)):
    for storage_quantity in data:
        create_storage_quantity(db, storage_quantity)

    return {"data": "Storage quantities added"}


@router.get('/{storage_id}', response_model=List[schemas.StorageQuantityData])
def read_storages_quantity(db: Session = Depends(get_db), storage_id: int = 2, month: str = 'all'):
    storages_quantity = get_storages_quantity(db, storage_id, month)

    if storages_quantity is None:
        raise HTTPException(status_code=404, detail="Storage quantity not found")

    return storages_quantity
