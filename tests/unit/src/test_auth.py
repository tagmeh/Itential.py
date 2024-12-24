import unittest
from unittest.mock import MagicMock, patch

from itential.src.auth import Auth


class TestAuth(unittest.TestCase):

    @classmethod
    @patch("itential.src.auth.Auth.authenticate")
    def setUpClass(cls, auth_mock: MagicMock) -> None:
        auth_mock.return_value = None  # Skips attempting to authenticate.

        # Using default vars
        cls.auth = Auth()

    def test_url(self):
        """
        Tests the Auth url setter method that should clean and standardize the url.
        """

        urls = [
            "  http://localhost:3000  ",
            "http://localhost:3000/",
            "   http://localhost:3000///   ",
        ]

        for url in urls:
            self.auth.url = url

            self.assertEqual(self.auth.url, "http://localhost:3000")

    def test_login_path(self):
        """
        Helper method to allow newer Itential**** versions to override the login url incase something changes.
        Test for coverage.
        """
        self.assertEqual(self.auth.get_login_path(), "/login/")
