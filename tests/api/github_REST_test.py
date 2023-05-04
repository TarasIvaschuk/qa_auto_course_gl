import pytest

from src.applications.api.github_client import github_client
from tests.constants import GitHubConstants


@pytest.mark.create_new_repo_data(owner=GitHubConstants.OWNER, repo=GitHubConstants.NEW_REPO)
class TestGitHubRestAPI:

    def test_search_existing_repo_status_code_success(self):
        query_params = {
            "q":f"{GitHubConstants.REPO} in:name"
        }
        response = github_client.search_repo(query_params)

        assert response.status_code == 200

    def test_search_existing_repo_total_count_gt_0(self):
        query_params = {
            "q":f"{GitHubConstants.REPO} in:name"
        }
        response = github_client.search_repo(query_params)

        assert response.json()['total_count'] > 0

    def test_seach_non_existing_repo_status_code_success(self):
        query_params = {
            "q":f"{GitHubConstants.NEW_REPO} in:name"
        }
        response = github_client.search_repo(query_params)

        assert response.status_code == 200

    def test_seach_non_existing_repo_count_eq_0(self):
        query_params = {
            "q":f"{GitHubConstants.NEW_REPO} in:name"
        }
        response = github_client.search_repo(query_params)

        assert response.json()['total_count'] == 0

    def test_create_new_repo_status_code_success(self, create_new_repo):
        response = create_new_repo

        assert response.status_code == 201

    def test_search_new_repo_total_count_gt_0(self, create_new_repo):
        query_params = {
            "q": f"{GitHubConstants.NEW_REPO} in:name"
        }
        response = github_client.search_repo(query_params)

        assert response.json()['total_count'] > 0

    def test_new_repo_full_name(self, create_new_repo):
        full_name = create_new_repo.json()['full_name']

        assert full_name == f'{GitHubConstants.OWNER}/{GitHubConstants.NEW_REPO}'

    def test_new_repo_description(self, create_new_repo):
        description = create_new_repo.json()['description']

        assert description == 'created with python'

    def test_update_new_repo_description_status_code_success(self, create_new_repo):
        data = {'description': 'updated with python!!!'}
        response = github_client.update_repo(
            GitHubConstants.OWNER, GitHubConstants.NEW_REPO, body=data)

        assert response.status_code == 200

    def test_new_repo_updated_description(self, create_new_repo):
        data = {'description': 'updated with python!!!'}
        response = github_client.update_repo(GitHubConstants.OWNER, GitHubConstants.NEW_REPO, body=data)

        assert response.json()['description'] == 'updated with python!!!'

    def test_delete_new_repo_status_code_success(self, create_new_repo):
        response = github_client.delete_repo(
            GitHubConstants.OWNER, GitHubConstants.NEW_REPO)

        assert response.status_code == 204

    def test_search_deleted_new_repo_status_code_success(self):
        query_params = {
            "q": f"{GitHubConstants.NEW_REPO} in:name"
        }
        response = github_client.search_repo(query_params)

        assert response.status_code == 200

    def test_search_deleted_new_repo_count_eq_0(self):
        query_params = {
            "q": f"{GitHubConstants.NEW_REPO} in:name"
        }
        response = github_client.search_repo(query_params)

        assert response.json()['total_count'] == 0
