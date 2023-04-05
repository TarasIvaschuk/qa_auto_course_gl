from src.config.conf import config

def test_user_age_is_not_43(user):
  print('check if user age is not 43')
  assert user.age != 43

def test_user_age_is_42(user):
  print('check if user age is 42')
  assert user.age == 42

def test_http_request():
   assert config.get('BASE_URL') == 'test.test.com'