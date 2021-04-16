from github import Github
from github.Repository import Repository
from github.Commit import Commit


class SearchService:
    def __init__(self, github_client: Github):
        self._github_client = github_client

    def search_repositories(self, query, limit) -> list:
        """Search for repositories and return formatted data."""
        repositories = self._github_client.search_repositories(query=query, **{'in': 'name'},)
        return [
            SearchService._format_repo(repository)
            for repository in repositories[:limit]
        ]

    @staticmethod
    def _format_repo(repository: Repository):
        commits = repository.get_commits()
        return {
            'url': repository.html_url,
            'name': repository.name,
            'owner': {
                'login': repository.owner.login,
                'url': repository.owner.html_url,
                'avatar_url': repository.owner.avatar_url,
            },
            'latest_commit': SearchService._format_commit(commits[0]) if commits else {},
        }

    @staticmethod
    def _format_commit(commit: Commit):
        return {
            'sha': commit.sha,
            'url': commit.html_url,
            'message': commit.commit.message,
            'author_name': commit.commit.author.name,
        }
