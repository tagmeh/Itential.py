import unittest
from unittest import TestCase
from unittest.mock import MagicMock

import requests

from src.exceptions import ApiError
from src.v2021_1 import Itential2021_1


class TestItential2021_1(TestCase):
    """Tests the Itential2021_1 class against a live local server."""

    @classmethod
    def setUpClass(cls):
        cls.should_skip = False
        # Check if the Local server is running and is the correct version for this test suite.
        try:
            response = requests.get("http://localhost:3000/version")

        except requests.exceptions.ConnectionError:
            cls.should_skip = True
            cls.reason = "Could not connect to server."

        else:
            if not response.ok:
                cls.should_skip = True
                cls.reason = "Server is not running."

            if "2021.1" not in response.json():
                cls.should_skip = True
                cls.reason = "Server is not the correct version."

    def setUp(self):
        if self.should_skip:
            self.skipTest(self.reason)

    def test_authentication_success(self):
        """Validates we can log into the Itential Server. Also tests the itential.call method innately."""
        itential = Itential2021_1(username="admin@pronghorn", password="admin", server_url="http://localhost:3000")
        self.assertTrue(itential.session.cookies.get("token"), "Authentication failed.")

    def test_authentication_failure(self):
        """Validates the Itential Server rejects invalid credentials."""
        with self.assertRaises(ApiError):  # Expecting a 401 Unauthorized
            itential = Itential2021_1(
                username="admin@pronghorn", password="wrong_password", server_url="http://localhost:3000"
            )

            self.assertFalse(itential.session.cookies.get("token"), "Authentication succeeded with wrong password.")

    def test_call_success(self):
        """Validates a successful call to the Itential Server."""
        itential = Itential2021_1(username="admin@pronghorn", password="admin", server_url="http://localhost:3000")
        response = itential.call(method="GET", endpoint="/workflow_engine/jobs/metrics")
        self.assertTrue(response.ok, "Call failed.")

    # TODO: Pending way to trigger except clause in the call method.
    # def test_call_failure(self):
    #     """Validates a failed call to the Itential Server."""
    #     with self.assertRaises(ApiError):
    #         itential = Itential2021_1(username="admin@pronghorn", password="admin", server_url="http://localhost:3000")
    #         # POST is not allowed on this endpoint.
    #         itential.call(method="POST", endpoint="/workflow_engine/jobs/metrics")

    def test_auto_re_authentication(self):
        """Validates the auto-re-authentication feature."""
        itential = Itential2021_1(username="admin@pronghorn", password="admin", server_url="http://localhost:3000")

        # Mocked in order to see itential.authenticate() was called.
        # Not overwriting the method's functionality.
        itential.authenticate = MagicMock(side_effect=itential.authenticate)

        itential.session.cookies.clear()  # Causes the first call to fail with a 401.

        response = itential.call(method="GET", endpoint="/workflow_engine/jobs/metrics")

        # Check if the itential.authenticate() method was called
        # The authentication method is called if the first call fails with a 401.
        itential.authenticate.assert_called_once()

        self.assertTrue(response.ok, "Auto-reauthentication failed.")
