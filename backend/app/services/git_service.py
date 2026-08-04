from pathlib import Path
from git import Repo


REPO_STORAGE = Path("storage/repos")


class GitService:

    def clone(self, clone_url: str, full_name: str) -> str:
        REPO_STORAGE.mkdir(parents=True, exist_ok=True)

        folder_name = full_name.replace("/", "__")

        destination = REPO_STORAGE / folder_name

        if destination.exists():
            print(f"Repository already exists: {destination}")
            return str(destination)

        print(f"Cloning {clone_url}")

        Repo.clone_from(
            clone_url,
            destination,
            depth=1,
        )

        print("Clone completed!")

        return str(destination)


git_service = GitService()