from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from controllers.products import get_products, get_product
from schemas import schemas
from models.database import get_db

router = APIRouter()


@router.get('/', response_model=List[schemas.Product])
def read_products(db: Session = Depends(get_db), storage_id: int | bool = False):
    products = get_products(db, storage_id)

    if products is None:
        raise HTTPException(status_code=404, detail="Products not found")

    return products


@router.get('/{product_id}', response_model=schemas.Product)
def read_product(db: Session = Depends(get_db), product_id: int = 1):
    product = get_product(db, product_id)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product
