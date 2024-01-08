#!/usr/bin/env python3
"""crete various tests for the
GithubOrgClient class"""

from client import GithubOrgClient
import utils
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, MagicMock


class TestGithubOrgClient(unittest.TestCase):
    """tests for the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch("client.get_json")
    def test_org(self, org_name: str,
                 mock_get: MagicMock) -> None:
        """test for GithubOrgClient.org"""
        expected = f"https://api.github.com/orgs/{org_name}"
        mock_get.return_value = MagicMock(return_value=expected)
        git_client = GithubOrgClient(org_name)
        result = git_client.org()
        self.assertEqual(result, expected)
        mock_get.assert_called_once_with(expected)
