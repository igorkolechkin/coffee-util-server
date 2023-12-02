from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from controllers.storages import get_storages, create_storage, get_storage
from schemas import schemas
from models.database import get_db

router = APIRouter()


@router.post('/', response_model=schemas.Storage)
def add_storage(storages: List[schemas.StorageCreate], db: Session = Depends(get_db)):
    for storage in storages:
        create_storage(db, storage)

    return {"data": "Storages added"}


@router.get('/', response_model=List[schemas.Storage])
def read_storages(db: Session = Depends(get_db)):
    storages = get_storages(db)

    if storages is None:
        raise HTTPException(status_code=404, detail="Storages not found")

    return storages


@router.get('/{storage_id}', response_model=schemas.StorageFull)
def read_storage(db: Session = Depends(get_db), storage_id: int = 1):
    storage = get_storage(db, storage_id)

    if storage is None:
        raise HTTPException(status_code=404, detail="Storage not found")

    return storage
