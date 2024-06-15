from models.product import Product
from sqlalchemy.orm import Session
from dto import product


def create_product(data: product.Product, db):
    prod = Product(name=data.name, category=data.category)

    try:
        db.add(prod)
        db.commit()
        db.refresh(prod)
    except Exception as e:
        print(e)

    return prod


def get_product(id: int, db):
    return db.query(Product).filter(Product.id == id).first()


def update_product(data: product.Product, db: Session, id: int):
    prod = db.query(Product).filter(Product.id == id).first()

    prod.name = data.name
    prod.category = data.category

    db.add(prod)
    db.commit()
    db.refresh(prod)

    return prod


def remove_product(id: int, db: Session):
    prod = db.query(Product).filter(Product.id == id).delete()
    db.commit()
    return prod
