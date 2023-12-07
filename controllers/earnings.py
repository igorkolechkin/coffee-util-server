from sqlalchemy import func, extract
from sqlalchemy.orm import Session
from models import models
from schemas import schemas


def get_earnings(db: Session, storage_id: int, month: str):
    return (db.query(models.Earnings)
            .filter(
                func.substring(models.Earnings.date, 6, 2) == month,
                models.Earnings.storage_id == storage_id
            )
            .first())


def set_earnings(db: Session, data: schemas.EarningsBase):
    existing_earnings = (
        db.query(models.Earnings)
        .filter(
            models.Earnings.date == data.date,
            models.Earnings.storage_id == data.storage_id
        )
        .first()
    )

    if existing_earnings:
        existing_earnings.cash = data.cash
        existing_earnings.card = data.card
        db.commit()
        db.refresh(existing_earnings)
        return 'Earning updated'
    else:
        db_earnings = models.Earnings(**data.model_dump())
        db.add(db_earnings)
        db.commit()
        db.refresh(db_earnings)
        return 'Earning added'
