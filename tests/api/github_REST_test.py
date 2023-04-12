from src.config.conf import config
from src.applications.api.github_client import github_client
import time

new_repo_name = 'taras_ivashchuk_test'
owner = 'TarasIvaschuk'
sec_to_wait = 2
description = 'created with python'


def test_search_existing_repos():
    response = github_client.search_repo('qa_auto_course_gl')
    assert response.status_code == 200
    assert response.json()['total_count'] > 0


def test_seach_non_existing_repos():
    # github won't let you have the repository with name starting with $$
    response = github_client.search_repo(new_repo_name)
    assert response.status_code == 200
    assert response.json()['total_count'] == 0



def test_create_new_repo():
    response = github_client.create_repo(
        new_repo_name, description=description)
    assert response.status_code == 201
    assert response.json()['full_name'] == f'{owner}/{new_repo_name}'


def test_search_newly_created_repo():
    time.sleep(sec_to_wait)
    response = github_client.search_repo(new_repo_name)
    assert response.status_code == 200
    assert response.json()['total_count'] > 0
    for d in response.json()['items']:
      if 'description' in d:
        desc = d['description']
    
    assert desc == description


description = 'updated description'
data = {"description": description}


def test_update_description_of_newly_created_repo():
    response = github_client.update_repo(owner, new_repo_name, data)
    assert response.status_code == 200


def test_description_of_newly_created_repo_is_updated():
    response = github_client.search_repo(new_repo_name)
    assert response.status_code == 200
    for d in response.json()['items']:
      if 'description' in d:
        desc = d['description']
    
    assert desc == description


def test_delete_newly_created_repo():
    response = github_client.delete_repo(
        owner, new_repo_name)
    assert response.status_code == 204


def test_search_deleted_newly_created_repo():
    time.sleep(sec_to_wait)
    response = github_client.search_repo(new_repo_name)
    assert response.status_code == 200
    assert response.json()['total_count'] == 0
