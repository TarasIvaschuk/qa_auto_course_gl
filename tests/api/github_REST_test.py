from src.applications.api.github_client import github_client
from tests.api.constants import Github_constants, Time_constants
import time


def test_search_existing_repos():
    response = github_client.search_repo(Github_constants.REPO.value)
    assert response.status_code == 200
    assert response.json()['total_count'] > 0


def test_seach_non_existing_repos():
    # github won't let you have the repository with name starting with $$
    response = github_client.search_repo(Github_constants.NEW_REPO.value)
    assert response.status_code == 200
    assert response.json()['total_count'] == 0


def test_create_new_repo(g_repo_description):
    response = github_client.create_repo(
        Github_constants.NEW_REPO.value, description=g_repo_description['desc'])
    assert response.status_code == 201
    assert response.json()[
        'full_name'] == f'{Github_constants.REPO_OWNER.value}/{Github_constants.NEW_REPO.value}'


def test_search_newly_created_repo(g_repo_description):
    time.sleep(Time_constants.SEC2.value)
    response = github_client.search_repo(Github_constants.NEW_REPO.value)
    assert response.status_code == 200
    assert response.json()['total_count'] > 0
    for d in response.json()['items']:
        if 'description' in d:
            desc = d['description']

    assert desc == g_repo_description['desc']


def test_update_description_of_newly_created_repo(g_repo_description):
    g_repo_description['desc'] = 'updated with python'
    data = {"description": g_repo_description['desc']}
    response = github_client.update_repo(
        Github_constants.REPO_OWNER.value, Github_constants.NEW_REPO.value, data)
    assert response.status_code == 200


def test_description_of_newly_created_repo_is_updated(g_repo_description):
    response = github_client.search_repo(Github_constants.NEW_REPO.value)
    assert response.status_code == 200
    for d in response.json()['items']:
        if 'description' in d:
            desc = d['description']

    assert desc == g_repo_description['desc']


def test_delete_newly_created_repo():
    response = github_client.delete_repo(
        Github_constants.REPO_OWNER.value, Github_constants.NEW_REPO.value)
    assert response.status_code == 204


def test_search_deleted_newly_created_repo():
    time.sleep(Time_constants.SEC2.value)
    response = github_client.search_repo(Github_constants.NEW_REPO.value)
    assert response.status_code == 200
    assert response.json()['total_count'] == 0
