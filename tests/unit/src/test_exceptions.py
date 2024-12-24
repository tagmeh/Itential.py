import unittest
from unittest.mock import MagicMock

from itential.src.exceptions import ApiError, NotSupportedError


class TestAuth(unittest.TestCase):

    def test_NotSupportedError(self):
        with self.assertRaises(NotSupportedError) as error:
            raise NotSupportedError("This feature is not supported at this time.")

        self.assertEqual(str(error.exception), "This feature is not supported at this time.")

    def test_ApiError(self):
        mock_response = MagicMock()
        mock_response.return_value.status_code = 500
        mock_response.resturn_value.json.return_value = {"payload": "data!"}

        with self.assertRaises(ApiError) as error:
            raise ApiError(mock_response.status_code, "The API call failed for some reason.", mock_response.json())

        self.assertEqual(
            str(error.exception),
            f"API Error {mock_response.status_code}: The API call failed for some reason. Error: {mock_response.json()}",
        )
