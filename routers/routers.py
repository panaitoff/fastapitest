from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import product as SERV_prod
from dto import product as dto_prod

router = APIRouter()


@router.post('/', tags=["product"])
async def create_prod(data: dto_prod.Product = None, db: Session = Depends(get_db)):
    return SERV_prod.create_product(data, db)


@router.get("/{id}", tags=['product'])
async def get_product(id: str = None, db: Session = Depends(get_db)):
    return SERV_prod.get_product(id, db)


@router.put("/{id}", tags=['product'])
async def upadate_product(id: str = None, data: dto_prod.Product = None, db: Session = Depends(get_db)):
    return SERV_prod.update_product(data, db, id)


@router.delete("/{id}", tags=["product"])
async def delete_product(id: str = None, db: Session = Depends(get_db)):
    return SERV_prod.remove_product(id, db)