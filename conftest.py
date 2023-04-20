import pytest
from src.applications.ui.github_ui_app import GitHubUI
from src.config.conf import CONFIG
from src.providers.service.browsers.browser_provider import BrowserProvider


class User:
    def __init__(self, age=33):
        self.age = age

    def remove(self):
        self.age = None


@pytest.fixture
def user():
    # before test
    print('User created')
    user = User(42)

    # pass user object to test
    yield user

    # after test
    print('User removed')
    user.remove()


@pytest.fixture(autouse=True, scope='class')
def global_vars():
    return {}


@pytest.fixture
def github_ui_app():
    browser = CONFIG.get("BROWSER")
    driver = BrowserProvider().get_driver(browser)

    github_ui = GitHubUI(driver)
    github_ui.launch()

    yield github_ui

    github_ui.quit()
