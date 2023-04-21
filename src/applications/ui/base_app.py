from selenium.webdriver.support.wait import WebDriverWait
from src.applications.constants import TimeConstants
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException    


class BaseExcepton(Exception):
  def __init__(self, msg):
    self.msg = msg


class SeleniumWrapper:
  def __init__(self, driver) -> None:
    self.driver = driver

  def click(self, loc):
    try:
      el = WebDriverWait(self.driver, timeout=TimeConstants.WAIT_SEC).until(lambda d: d.find_element(*loc))
      el.click()
    except TimeoutException:
      raise BaseException (f'{loc} is not found!')

  def send_keys(self, loc, text):
    try:
      el = WebDriverWait(self.driver, timeout=TimeConstants.WAIT_SEC).until(lambda d: d.find_element(*loc))
      el.send_keys(text)
    except:
      raise BaseException (f'{loc} is not found')

  def wait_for_el(self, loc, timeout = TimeConstants.WAIT_SEC):
    # todo return some seleniom element wrapper
    try:
      el = WebDriverWait(self.driver, timeout=timeout).until(lambda d: d.find_element(*loc))
      return el
    except:
        raise BaseException (f'{loc} is not found')
