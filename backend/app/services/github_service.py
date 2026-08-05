import httpx

from app.core.config import settings


class GitHubService:

    async def get_repository(self, full_name: str):

        url = f"{settings.GITHUB_API}/repos/{full_name}"

        headers = {}

        if settings.GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)

        response.raise_for_status()

        return response.json()

    async def get_issues(self, repository: str):

        url = f"{settings.GITHUB_API}/repos/{repository}/issues"

        headers = {}

        if settings.GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"

        async with httpx.AsyncClient() as client:
            response = await client.get(
                url,
                headers=headers,
                params={
                    "state": "all",
                    "per_page": 100,
                },
            )

        response.raise_for_status()

        return response.json()


github_service = GitHubService()