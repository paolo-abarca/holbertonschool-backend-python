#!/usr/bin/env python3
"""
test client modules
"""
from client import GithubOrgClient
import client
from parameterized import parameterized, parameterized_class
from unittest.mock import PropertyMock, patch, Mock, call
import unittest
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Github org client class
    """

    @parameterized.expand(
        [
            ("google", {"google": True}),
            ("abc", {"abc": True}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org, expected, mock_request):
        """
        test org method
        """
        mock_request.return_value = expected
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org, expected)
        mock_request.assert_called_once()


if __name__ == "__main__":
    unittest.main()
