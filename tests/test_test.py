from src.config.conf import config
from src.applications.api.github_client import github_client


def test_user_age_is_not_43(user):
    print('check if user age is not 43')
    assert user.age != 43


def test_user_age_is_42(user):
    print('check if user age is 42')
    assert user.age == 42


def test_http_request():
    assert config.get('BASE_URL') == 'test.test.com'


def test_search_existing_repo_on_github():
    response = github_client.search_repo('some_exist_repo')
    assert response == 'some_exist_repo'


def test_seach_non_existing_repo_on_github():
    response = github_client.search_repo('some_non_exist_repo')
    assert response == 'some_non_exist_repo'
