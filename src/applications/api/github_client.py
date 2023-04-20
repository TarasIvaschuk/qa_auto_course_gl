from dotenv import load_dotenv
import os
import requests
import urllib.parse as url_parse
from src.config.conf import CONFIG
from src.applications.constants import GitHubURL


# to load the token from the .env
load_dotenv()


class GitHubClient():
    '''
      the client uses github REST API 
      generate personal token manually
      give the token read and write permissions for administration
      create .env in current directory
      write in the .env GITHUB_TOKEN=your_token
      https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
    '''

    def __init__(self):
        self.token = os.environ.get('GITHUB_TOKEN')
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json"
        }

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers):
        self._headers = headers

    def _build_url(self, basic_url, query_params):
        url_parse.quote('_', safe='')
        query_string = url_parse.urlencode(
            query_params, quote_via=url_parse.quote)
        question_mark = '?'
        return basic_url + question_mark + query_string

    def search_repo(self, repo_name):
        # todo add query params constructor string
        query_params = {
            "q": f"{repo_name} in:name"
        }
        url = self._build_url(GitHubURL.RestAPI.Repo.SEARCH, query_params)
        res = requests.get(url, headers=self.headers)
        return res

    def create_repo(self, body):
        res = requests.post(GitHubURL.RestAPI.Repo.CREATE, headers = self.headers, json = body)
        return res

    def delete_repo(self, owner, repo):
        delete_repo_url = GitHubURL.RestAPI.Repo.DELETE + "/" + owner + "/" + repo
        res = requests.delete(delete_repo_url, headers=self.headers)
        return res

    def update_repo(self, owner, repo, body):
        update_repo_url = GitHubURL.RestAPI.Repo.UPDATE + "/" + owner + "/" + repo
        res = requests.patch(update_repo_url, headers=self.headers, json=body)
        return res


github_client = GitHubClient()
