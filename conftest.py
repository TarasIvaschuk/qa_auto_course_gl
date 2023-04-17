import pytest

class User:
  def __init__ (self, age=33):
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


@pytest.fixture(scope = 'module')
def g_repo_description():
    return {'desc':"created with python"}