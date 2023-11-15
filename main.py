from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.database import engine
from models import models
from routers.storages import router as storages_router
from routers.products import router as products_router
from routers.storageQuantity import router as storage_quantity_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# TODO
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=storages_router,
    prefix='/storages'
)

app.include_router(
    router=products_router,
    prefix='/products'
)

app.include_router(
    router=storage_quantity_router,
    prefix='/storage_quantity'
)
