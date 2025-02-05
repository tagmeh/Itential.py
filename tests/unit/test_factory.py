import unittest
from unittest.mock import MagicMock, patch

from src import ItentialVersion, create_itential
from src.v2021_1 import Itential2021_1


class TestItential(unittest.TestCase):

    @patch("src.base.itential.Itential.authenticate")
    def test_create_itential2021_1(self, auth_mock: MagicMock) -> None:
        auth_mock.return_value = None  # Skips attempting to authenticate.

        itential2021_1 = create_itential(version=ItentialVersion.V2021_1)
        self.assertIsInstance(itential2021_1, Itential2021_1)

    # @patch("src.base.itential.Itential.authenticate")
    # def test_create_itential2023_1(self, auth_mock: MagicMock) -> None:
    #     auth_mock.return_value = None  # Skips attempting to authenticate.

    # itential2023_1 = Itential.create(version=ItentialVersion.V2023_1)
    # self.assertIsInstance(itential2023_1, Itential2023_1)
