
from contextlib import asynccontextmanager
from app.api.routes.repositories import router as repository_router
from fastapi import FastAPI
from app.api.routes.indexing import router as indexing_router
from app.core.config import settings
from app.db.database import ping_database
from app.api.routes.search import router as search_router
from app.api.routes.issues import router as issues_router
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

print("Registering indexing router...")
app.include_router(indexing_router)
app.include_router(search_router)
print("Repository routes:", repository_router.routes)
print("Indexing routes:", indexing_router.routes)
print("Search routes:", search_router.routes)
print("Done registering routers.")
app.include_router(issues_router)
@app.get("/")
async def root():
    return {"message": "Welcome to IssueLens"}


