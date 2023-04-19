import pytest
from src.applications.ui.github_ui_app import GitHub_UI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


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
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    github_ui = GitHub_UI(driver)
    github_ui.launch()

    yield github_ui

    github_ui.quit()
