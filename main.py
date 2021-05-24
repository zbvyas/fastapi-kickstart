from fastapi import FastAPI
from routers import pets
from database import models
from database.connection import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(pets.router)

@app.get("/")
async def root():
    return {"message": "Server is Running"}