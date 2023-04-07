from src.config.conf import config
from src.applications.api.github_client import github_client

def test_user_age_is_not_43(user):
    print('check if user age is not 43')
    assert user.age != 43


def test_user_age_is_42(user):
    print('check if user age is 42')
    assert user.age == 42


def test_base_test_url():
    assert config.get('BASE_TEST_URL') == 'test_url'


def test_search_existing_repos_on_github():
    response = github_client.search_repos_by_name('TarasIvaschuk')
    assert response.json()['total_count'] > 0
    assert response.status_code == 200


def test_search_existing_repos_on_github():
    response = github_client.search_repos_by_name('sergii-butenko-gl')
    assert response.json()['total_count'] > 0
    assert response.status_code == 200


def test_seach_non_existing_repos_on_github():
    # github won't let you have the repository with name starting with $$
    response = github_client.search_repos_by_name('$$')
    assert response.status_code == 422
    
