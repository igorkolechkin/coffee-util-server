from decimal import Decimal
from typing import List

from pydantic import BaseModel


class StorageBase(BaseModel):
    name: str


class StorageCreate(StorageBase):
    pass


class Storage(StorageBase):
    id: int

    class Config:
        from_attributes = True


class StorageFull(Storage):
    id: int
    rent: int
    communal: int
    sim_card: int
    employee_salaries: int
    prosto_pay: int


class ProductBase(BaseModel):
    name: str
    current_price: Decimal
    to_storages: List[int]


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True


class StorageQuantityBase(BaseModel):
    storage_id: int
    product_id: int
    price: Decimal
    count: int
    date: str


class StorageQuantityCreate(StorageQuantityBase):
    pass


class StorageQuantity(StorageQuantityBase):
    id: int

    class Config:
        from_attributes = True


class StorageQuantityData(BaseModel):
    product_id: int
    price: Decimal
    count: int
    date: str


class ProductBaseData(BaseModel):
    id: int
    price: Decimal
    count: int
