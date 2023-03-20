from src.config.conf import Config

def test_user_age_is_43(user):
  print('check if user age is 43')
  assert user.age == 43

def test_user_age_is_42(user):
  print('check if user age is 42')
  assert user.age == 42

def test_http_request():
   assert Config().get('BASE_URL') == 'test.test.com'