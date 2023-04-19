from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.config.conf import CONFIG
from selenium.webdriver.common.by import By
import time
from src.applications.constants import GitHub as github_c


class Sign_in_page:
  def __init__(self, driver) -> None:
    self.USERNAME_FLD = 'login_field' # id
    self.PASSWORD_FLD = 'password' #id
    self.SIGN_IN_BTN = 'password' # name
    self.URL = '/login'
    self.driver = driver
  
  def go_to(self):
    self.driver.get(github_c.UI.BASE_URL+ self.URL)

  def try_sign_in(self, username, password):
    username_fld = self.driver.find_element(By.ID, self.USERNAME_FLD)
    username_fld.send_keys(username)
    time.sleep(2)


    password_fld = self.driver.find_element(By.ID, self.PASSWORD_FLD)
    password_fld.send_keys(password)
    time.sleep(2)


    sign_in_btn  = self.driver.find_element(By.NAME, self.SIGN_IN_BTN)
    sign_in_btn.click()
    time.sleep(2)

    return self

  def check_error_message(self):
    # todo
    return "Error" == "Error"