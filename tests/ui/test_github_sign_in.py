import pytest  
from src.applications.ui.github_ui_app import githubui

@pytest.fixture
def browser():
  githubui.launch()
  yield githubui
  githubui.close()


def test_failed_login(browser):
  browser.go_to_login_page()
  browser.try_login()
  assert browser.check_error_message()