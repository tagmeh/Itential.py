import unittest
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src import ItentialVersion, create_itential
from src.v2021_1 import Itential2021_1


class TestItential(TestCase):

    @patch("src.base.itential.Itential.authenticate")
    def test_create_itential(self, mock_call: MagicMock):
        mock_call.return_value = None

        itential2021_1 = create_itential(version=ItentialVersion.V2021_1)

        self.assertIsInstance(itential2021_1, Itential2021_1)


if __name__ == "__main__":
    unittest.main()
