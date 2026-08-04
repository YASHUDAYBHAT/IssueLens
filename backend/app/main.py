
from contextlib import asynccontextmanager
from app.api.routes.repositories import router as repository_router
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

print("Registering repository router...")
app.include_router(repository_router)
print("Repository router registered!")
@app.get("/")
async def root():
    return {"message": "Welcome to IssueLens"}


