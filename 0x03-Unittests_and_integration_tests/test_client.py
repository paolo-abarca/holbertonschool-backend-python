#!/usr/bin/env python3
"""
Familiarize yourself with the client.GithubOrgClient class
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    declare the TestGithubOrgClient(unittest.TestCase) class
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        implement method test_org with test org
        """
        url = "https://api.github.com/orgs/{}".format(org_name)
        org_client = GithubOrgClient(org_name)
        org_client.org()
        mock_get_json.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
