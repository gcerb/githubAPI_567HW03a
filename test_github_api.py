import unittest
from unittest.mock import patch
from github_api import get_repos, get_commit_count, get_repos_and_commits

class TestGitHubApi(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_get_repos(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"name": "testrepo"}]
        self.assertEqual(get_repos("fakeuser"), ["testrepo"])

    @patch("github_api.requests.get")
    def test_get_commit_count(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [1, 2, 3]
        self.assertEqual(get_commit_count("fakeuser", "repo"), 3)

    @patch("github_api.get_repos")
    @patch("github_api.get_commit_count")
    def test_get_repos_and_commits(self, mock_commit, mock_repos):
        mock_repos.return_value = ["repo1"]
        mock_commit.return_value = 5
        self.assertEqual(get_repos_and_commits("fakeuser"), [{"repo": "repo1", "commits": 5}])

if __name__ == "__main__":
    unittest.main()
