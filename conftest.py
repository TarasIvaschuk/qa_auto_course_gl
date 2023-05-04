import pytest
import time

from src.applications.ui.github_ui_app import GitHubUI
from src.config.conf import CONFIG
from src.providers.service.browsers.browser_provider import BrowserProvider
from src.applications.api.github_client import github_client


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


@pytest.fixture(scope="class")
def create_new_repo(request): 
    data = request.node.get_closest_marker("create_new_repo_data").kwargs 
    owner = data['owner']
    repo = data['repo']
    body = {
        "name": repo,
        "description": "created with python"
    }
    response = github_client.create_repo(body)
    time.sleep(5)
    
    yield response

    github_client.delete_repo(owner, repo)



