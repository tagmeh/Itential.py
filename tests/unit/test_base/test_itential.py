import unittest
from unittest.mock import MagicMock, patch

from src.base import Itential


class TestItential(unittest.TestCase):

    @classmethod
    @patch("src.base.itential.Itential.authenticate")
    def setUpClass(cls, auth_mock: MagicMock) -> None:
        auth_mock.return_value = None  # Skips attempting to authenticate.

        cls.itential = Itential()

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
            self.itential.url = url

            self.assertEqual(self.itential.url, "http://localhost:3000")

    def test_login_path(self):
        """
        Helper method to allow newer Itential**** versions to override the login url incase something changes.
        Test for coverage.
        """
        self.assertEqual(self.itential.get_login_path(), "/login/")
