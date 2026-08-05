from fastapi import APIRouter
from app.models.issue_index_request import IssueIndexRequest
from app.indexing.issue_index_service import issue_index_service
from app.models.issue_search_request import IssueSearchRequest
from app.services.issue_search_service import issue_search_service

from app.models.issue_request import (
    IssueImportRequest,
)

from app.repositories.issue_repository import (
    issue_repository,
)

from app.services.github_service import (
    github_service,
)

router = APIRouter(
    prefix="/issues",
    tags=["Issues"],
)


@router.post("/import")
async def import_issues(
    request: IssueImportRequest,
):

    github_issues = await github_service.get_issues(
        request.repository
    )

    documents = []

    for issue in github_issues:

        if "pull_request" in issue:
            continue

        documents.append(
            {
                "github_id": issue["id"],
                "repository": request.repository,
                "number": issue["number"],
                "title": issue["title"],
                "body": issue["body"],
                "state": issue["state"],
                "url": issue["html_url"],
            }
        )

    await issue_repository.create_many(
        documents
    )

    return {
        "imported": len(documents)
    }

@router.post("/index")
async def index_issues(
    request: IssueIndexRequest,
):

    issues = await issue_repository.find_by_repository(
        request.repository
    )

    count = issue_index_service.index(
        issues
    )

    return {
        "message": "Issues indexed successfully",
        "indexed": count,
    }

@router.post("/search")
async def search_issues(
    request: IssueSearchRequest,
):

    results = issue_search_service.search(
        request.query,
        request.k,
    )

    response = []

    for score, issue in results:

        response.append(
            {
                "score": round(score, 4),
                "issue_number": issue["number"],
                "title": issue["title"],
                "repository": issue["repository"],
                "url": issue["url"],
            }
        )

    return {
        "query": request.query,
        "results": response,
    }

