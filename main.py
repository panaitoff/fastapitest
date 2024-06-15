import uvicorn
from fastapi import FastAPI
from database import SessionLocal, engine, Base

from routers import routers as ProductRouter

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(ProductRouter.router, prefix='/product')


if __name__ == "__main__":
    uvicorn.run("main:app")
