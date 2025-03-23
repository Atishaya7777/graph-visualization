from fastapi import APIRouter, Depends
from core.schemas.schema import Item, ItemCreate
from core.models.database import SessionLocal
from core.models.database import Base
from sqlalchemy.orm import Session

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/items", response_model=list[Item])
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()


@router.post("/items", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
