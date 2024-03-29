from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.config.conf import CONFIG
from selenium.webdriver.common.by import By
import time
from src.applications.constants import GitHubURL
from src.applications.constants import TimeConstants


class Sign_in_page:
  def __init__(self, app) -> None:
    self.FAIL_ATTEMPTS_CONTAINER = By.CSS_SELECTOR, '.logged-out'
    self.USERNAME_FLD = By.ID,'login_field'
    self.PASSWORD_FLD = By.ID, 'password'
    self.SIGN_IN_BTN = By.NAME,'commit'
    self.ERR_MSG = "there have been several failed attempts"
    self.URL = '/login'
    self.app = app
  
  def go_to(self):
    self.app.driver.get(GitHubURL.UI.BASE_URL+ self.URL)

  def try_sign_in(self, username, password):
    self.app.send_keys(self.USERNAME_FLD, username)
    time.sleep(TimeConstants.WAIT_SEC)
    self.app.send_keys(self.PASSWORD_FLD, password)
    time.sleep(TimeConstants.WAIT_SEC)
    self.app.click(self.SIGN_IN_BTN)
    time.sleep(TimeConstants.WAIT_SEC)
    return self

  def check_error_message(self):
    err_container = self.app.wait_for_el(self.FAIL_ATTEMPTS_CONTAINER,timeout = 5)
    # todo when the ElementWrapper is ready
    err_msg = err_container.find_element(By.TAG_NAME, 'p').text
    return self.ERR_MSG in err_msg.casefold()