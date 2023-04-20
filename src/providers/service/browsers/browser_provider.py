from src.providers.service.browsers.lib.chrome_wrapper import ChromeWrapper
from src.providers.service.browsers.lib.ff_wrapper import FFWrapper


class BrowserProvider:
  BROWSER_MAPPER = {
    'chrome': ChromeWrapper,
    'ff': FFWrapper
  }

  def __init__(self):
    pass

  def get_driver(self, browser): 
    browser_wrapper = self.BROWSER_MAPPER.get(browser)
    if browser_wrapper is None:
      raise NotImplementedError(f'Browser {browser} is not supported')
    
    driver = browser_wrapper.get_driver()
    return driver
      
