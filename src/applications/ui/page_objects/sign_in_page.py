from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.config.conf import CONFIG
from selenium.webdriver.common.by import By
import time
from src.applications.constants import GitHubURL


class Sign_in_page:
  def __init__(self, app) -> None:
    self.USERNAME_FLD = By.ID,'login_field'
    self.PASSWORD_FLD = By.ID, 'password'
    self.SIGN_IN_BTN = By.NAME,'password'
    self.URL = '/login'
    self.app = app
  
  def go_to(self):
    self.app.driver.get(GitHubURL.UI.BASE_URL+ self.URL)

  def try_sign_in(self, username, password):
    username_fld = self.app.driver.find_element(*self.USERNAME_FLD)
    username_fld.send_keys(username)
    time.sleep(2)


    password_fld = self.app.driver.find_element(*self.PASSWORD_FLD)
    password_fld.send_keys(password)
    time.sleep(2)


    sign_in_btn  = self.app.driver.find_element(*self.SIGN_IN_BTN)
    sign_in_btn.click()
    time.sleep(2)

    return self

  def check_error_message(self):
    # todo
    return "Error" == "Error"