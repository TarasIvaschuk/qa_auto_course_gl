from src.applications.ui.page_objects.sign_in_page import Sign_in_page
from src.config.conf import CONFIG
from src.applications.constants import GitHubURL
from src.applications.ui.selenium_wrapper import SeleniumWrapper

class GitHubUI(SeleniumWrapper):
  def __init__(self, driver) -> None:
    super().__init__(driver)
    self.SIGN_IN_PAGE = Sign_in_page(self)

  def launch(self):
    self.driver.get(GitHubURL.UI.BASE_URL)
    return self

  def quit(self):
    self.driver.quit()
    return self
