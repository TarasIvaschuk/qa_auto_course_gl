from src.applications.ui.page_objects.sign_in_page import Sign_in_page
from src.config.conf import CONFIG
from src.applications.constants import GitHub as github_c

class GitHubUI:
  def __init__(self, driver) -> None:
    self.driver = driver
    self.SIGN_IN_PAGE = Sign_in_page(driver)
    # selp.SIGN_UP_PAGE = ...

  def launch(self):
    self.driver.get(github_c.UI.BASE_URL)
    return self

  def quit(self):
    self.driver.quit()
    return self
