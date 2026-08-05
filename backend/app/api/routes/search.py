from fastapi import APIRouter

from app.models.search_request import SearchRequest
from app.services.search_service import search_service

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.post("/")
async def search(
    request: SearchRequest,
):

    results = search_service.search(
        request.query,
        request.k,
    )

    response = []

    for score, chunk in results:

        response.append(
            {
                "score": score,
                "qualified_name": chunk.qualified_name,
                "file_path": chunk.file_path,
                "start_line": chunk.start_line,
                "end_line": chunk.end_line,
            }
        )

    return {
        "results": response
    }