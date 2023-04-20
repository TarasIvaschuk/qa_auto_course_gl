# todo to load the urls from config

class GitHubURL:
  class RestAPI:
    class Repo:
          BASE_URL = "https://api.github.com"
          SEARCH = f"{BASE_URL}/search/repositories"
          CREATE = f"{BASE_URL}/user/repos"
          DELETE = f"{BASE_URL}/repos"
          UPDATE = f"{BASE_URL}/repos"
  class UI:
    BASE_URL = "https://github.com"
