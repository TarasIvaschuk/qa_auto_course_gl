import pytest
# from src.applications.ui.github_ui_app import github_ui
from src.applications.ui.page_objects.sign_in_page import Sign_in_page


def test_failed_login(github_ui_app):
  sign_in_page = github_ui_app.SIGN_IN_PAGE
  sign_in_page.go_to()
  sign_in_page.try_sign_in('username', 'password')
  assert sign_in_page.check_error_message()
