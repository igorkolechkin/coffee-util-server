from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, ARRAY
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Storage(Base):
    __tablename__ = 'storages'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    rent = Column(Integer)
    communal = Column(Integer)
    sim_card = Column(Integer)
    employee_salaries = Column(Integer)
    prosto_pay = Column(Integer)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    current_price = Column(Numeric)
    to_storages = Column(ARRAY(Integer))


class StorageQuantity(Base):
    __tablename__ = 'storageQuantities'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    storage_id = Column(Integer, ForeignKey('storages.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    price = Column(Numeric)
    count = Column(Integer)
    date = Column(String)
