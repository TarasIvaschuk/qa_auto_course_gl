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

