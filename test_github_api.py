import unittest
from unittest.mock import patch, MagicMock
from github_api import get_repos, get_commit_count, get_repos_and_commits

class TestGitHubApiMocked(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_get_repos_mocked(self, mock_get):
        # Mock response from GitHub API for repos
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_get.return_value = mock_response

        result = get_repos("fakeuser")
        self.assertEqual(result, ["repo1", "repo2"])

    @patch("github_api.requests.get")
    def test_get_commit_count_mocked(self, mock_get):
        # Mock response from GitHub API for commits
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"sha": 1}, {"sha": 2}, {"sha": 3}]
        mock_get.return_value = mock_response

        result = get_commit_count("fakeuser", "repo1")
        self.assertEqual(result, 3)

    @patch("github_api.get_repos")
    @patch("github_api.get_commit_count")
    def test_get_repos_and_commits_mocked(self, mock_commit_count, mock_get_repos):
        # Mock the helper functions instead of requests
        mock_get_repos.return_value = ["repo1", "repo2"]
        mock_commit_count.side_effect = [5, 10]  # repo1 has 5 commits, repo2 has 10

        result = get_repos_and_commits("fakeuser")
        self.assertEqual(result, [
            {"repo": "repo1", "commits": 5},
            {"repo": "repo2", "commits": 10}
        ])

if __name__ == "__main__":
    unittest.main()
