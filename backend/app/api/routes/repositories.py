
from fastapi import APIRouter

from app.models.request import RepositoryImportRequest
from app.repositories.repository_repository import repository_repository
from app.services.github_service import github_service

router = APIRouter(prefix="/repositories", tags=["Repositories"])


@router.post("/import")
async def import_repository(request: RepositoryImportRequest):

    repo = await github_service.get_repository(request.repository)

    document = {
            "github_id": repo["id"],
            "owner": repo["owner"]["login"],
            "name": repo["name"],
            "full_name": repo["full_name"],
            "description": repo["description"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "open_issues": repo["open_issues_count"],

            # NEW
            "clone_url": repo["clone_url"],
            "status": "imported",
            "local_path": None,

    }

    mongo_id = await repository_repository.create(document)

    return {
        "message": "Repository imported successfully",
        "id": mongo_id,
    }