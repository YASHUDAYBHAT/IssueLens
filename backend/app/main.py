
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.db.database import ping_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(" Starting IssueLens...")

    try:
        await ping_database()
        print(" Connected to MongoDB Atlas")
    except Exception as e:
        print(" MongoDB Connection Failed")
        print(e)

    yield

    print(" Shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {"message": "Welcome to IssueLens"}