from sqlalchemy import Column, ForeignKey, Integer, String, Numeric

from .database import Base


class Storage(Base):
    __tablename__ = 'storages'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    current_price = Column(Numeric)


class StorageQuantity(Base):
    __tablename__ = 'storageQuantities'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    storage_id = Column(Integer, ForeignKey('storages.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    price = Column(Numeric)
    count = Column(Integer)
    date = Column(String)
