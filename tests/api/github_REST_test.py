from src.applications.api.github_client import github_client
from tests.constants import TimeConstants
import time


class TestGitHubRestAPI:
    '''
    To share variables between each tests
    is not possible with the help of class attributes
    so global fixture (conftest.py) is used instead 
    '''
    RESPONSE = 'response'
    TOTAL_COUNT = 'total_count'
    FULL_NAME = 'full_name'
    DESCRIPTION = 'description'
    ITEMS = 'items'
    REPO_OWNER = 'TarasIvaschuk'
    NEW_REPO = 'tarasivashchuktest'
    REPO = 'qa_auto_course_gl'

    def test_search_existing_repo_status_code_success(self, global_vars):
        response = github_client.search_repo(self.REPO)
        global_vars[self.RESPONSE] = response.json()
        assert response.status_code == 200

    def test_search_existing_repo_total_count_gt_0(self, global_vars):
        assert global_vars.get(self.RESPONSE).get(self.TOTAL_COUNT) > 0

    def test_seach_non_existing_repo_status_code_success(self, global_vars):
        response = github_client.search_repo(self.NEW_REPO)
        global_vars[self.RESPONSE] = response.json()
        assert response.status_code == 200

    def test_seach_non_existing_repo_count_eq_0(self, global_vars):
        assert global_vars.get(self.RESPONSE).get(self.TOTAL_COUNT) == 0

    def test_create_new_repo_status_code_success(self, global_vars):
        global_vars[self.DESCRIPTION] = "created with python"
        body = {
            "name": self.NEW_REPO,
            "description": global_vars.get(self.DESCRIPTION)
        }
        response = github_client.create_repo(body)
        assert response.status_code == 201

    def test_search_new_repo_total_count_gt_0(self, global_vars):
        time.sleep(TimeConstants.WAIT_SEC)
        response = github_client.search_repo(self.NEW_REPO)
        global_vars[self.RESPONSE] = response.json()
        assert global_vars.get(self.RESPONSE).get(self.TOTAL_COUNT) > 0

    def test_new_repo_full_name(self, global_vars):
        response = global_vars.get(self.RESPONSE)
        for d in response.get(self.ITEMS):
            if self.FULL_NAME in d:
                full_name = d.get(self.FULL_NAME)

        assert full_name == f'{self.REPO_OWNER}/{self.NEW_REPO}'

    def test_new_repo_description(self, global_vars):
        time.sleep(TimeConstants.WAIT_SEC)
        response = global_vars.get(self.RESPONSE)
        for d in response.get(self.ITEMS):
            if self.DESCRIPTION in d:
                desc = d.get(self.DESCRIPTION)
        assert desc == global_vars.get(self.DESCRIPTION)

    def test_update_new_repo_description_status_code_success(self, global_vars):
        global_vars[self.DESCRIPTION] = 'updated with python'
        data = {self.DESCRIPTION: global_vars.get(self.DESCRIPTION)}
        response = github_client.update_repo(
            self.REPO_OWNER, self.NEW_REPO, data)
        global_vars[self.RESPONSE] = response.json()
        assert response.status_code == 200

    def test_new_repo_updated_description(self, global_vars):
        response = global_vars.get(self.RESPONSE)
        assert response.get(self.DESCRIPTION) == global_vars.get(
            self.DESCRIPTION)

    def test_delete_new_repo_status_code_success(self):
        response = github_client.delete_repo(
            self.REPO_OWNER, self.NEW_REPO)
        assert response.status_code == 204

    def test_search_deleted_new_repo_status_code_success(self, global_vars):
        time.sleep(TimeConstants.WAIT_SEC)
        response = github_client.search_repo(self.NEW_REPO)
        global_vars[self.RESPONSE] = response.json()
        assert response.status_code == 200

    def test_search_deleted_new_repo_count_eq_0(self, global_vars):
        time.sleep(TimeConstants.WAIT_SEC)
        assert global_vars.get(self.RESPONSE).get(self.TOTAL_COUNT) == 0
