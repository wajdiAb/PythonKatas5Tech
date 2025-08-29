import unittest
from unittest.mock import patch, Mock
from katas.github_user_fetcher import fetch_github_user, get_user_repositories_count
import requests

class TestGithubUserFetcher(unittest.TestCase):

    @patch('katas.github_user_fetcher.requests.get')
    def test_fetch_github_user_success(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            'login': 'octocat',
            'name': 'The Octocat',
            'public_repos': 8,
            'followers': 9999
        }
        mock_get.return_value = mock_response

        result = fetch_github_user('octocat')
        self.assertEqual(result, {
            'login': 'octocat',
            'name': 'The Octocat',
            'public_repos': 8,
            'followers': 9999
        })

    @patch('katas.github_user_fetcher.requests.get')
    def test_fetch_github_user_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        result = fetch_github_user('unknownuser')
        self.assertIsNone(result)

    @patch('katas.github_user_fetcher.requests.get')
    def test_fetch_github_user_invalid_json(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response

        result = fetch_github_user('octocat')
        self.assertIsNone(result)

    @patch('katas.github_user_fetcher.fetch_github_user')
    def test_get_user_repositories_count_success(self, mock_fetch):
        mock_fetch.return_value = {
            'login': 'octocat',
            'name': 'The Octocat',
            'public_repos': 8,
            'followers': 9999
        }
        count = get_user_repositories_count('octocat')
        self.assertEqual(count, 8)

    @patch('katas.github_user_fetcher.fetch_github_user')
    def test_get_user_repositories_count_user_not_found(self, mock_fetch):
        mock_fetch.return_value = None
        count = get_user_repositories_count('unknownuser')
        self.assertEqual(count, 0)

    @patch('katas.github_user_fetcher.fetch_github_user')
    def test_get_user_repositories_count_missing_field(self, mock_fetch):
        mock_fetch.return_value = {
            'login': 'octocat',
            'name': 'The Octocat',
            'followers': 9999
            # 'public_repos' missing
        }
        count = get_user_repositories_count('octocat')
        self.assertEqual(count, 0)

if __name__ == '__main__':
    unittest.main()