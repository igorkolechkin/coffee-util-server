from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from controllers.earnings import set_earnings, get_earnings
from schemas import schemas
from models.database import get_db

router = APIRouter()


@router.post('/')
def add_earnings(data: schemas.EarningsBase, db: Session = Depends(get_db)):
    response = set_earnings(db, data)

    return {'data': response}


@router.get('/', response_model=schemas.EarningsBase)
def read_earnings(db: Session = Depends(get_db), storage_id: int = 1, month: str = ''):
    earnings = get_earnings(db, storage_id, month)

    if earnings is None:
        raise HTTPException(status_code=404, detail='Storage not found')

    return earnings
