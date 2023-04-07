from dotenv import load_dotenv
import os
import requests
import urllib.parse as url_parse
from src.config.conf import config



# load the token from the .env
load_dotenv()

class Github_client():
    '''
      the client uses github REST API 
      generate personal token manually
      create .env in current directory
      write in the .env GITHUB_TOKEN=your_token
      https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
    '''

    def __init__(self):
        self.token = os.environ.get('GITHUB_TOKEN')

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    def _build_url(self, basic_url, query_params):
        query_string = url_parse.urlencode(
            query_params, quote_via=url_parse.quote)
        question_mark = '?'
        return basic_url + question_mark + query_string

    def search_repos_by_name(self, repo_name):
        query_params = {
            "q": f"user:{repo_name}"
        }
        basic_search_repo_url = config.get('GITHUB_BASIC_SEARCH_REPO_URL')
        url = self._build_url(basic_search_repo_url, query_params)
        res = requests.get(url, headers={
            "auth": self._token
        })
        return res

        print('You are logged out')


github_client = Github_client()
