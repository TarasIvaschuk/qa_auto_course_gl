from src.applications.ui.page_objects.sign_in_page import Sign_in_page
from src.config.conf import CONFIG

class GitHub_UI:
  def __init__(self, driver) -> None:
    self.driver = driver
    self.SIGN_IN_PAGE = Sign_in_page(driver)
    # selp.SIGN_UP_PAGE = ...

  def launch(self):
    self.driver.get(CONFIG.get("GITHUB_BASE_URL_UI"))
    return self

  def close(self):
    self.driver.close()
    return self
