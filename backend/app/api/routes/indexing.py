from fastapi import APIRouter

router = APIRouter(
    prefix="/index",
    tags=["Indexing"],
)

@router.get("/test")
async def test():
    return {"status": "ok"}