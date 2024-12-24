import unittest
from unittest.mock import MagicMock, patch

from itential import Itential
from itential.src.iap_versions.v2021_1 import Itential2021_1
from itential.src.versions import ItentialVersion


class TestItential(unittest.TestCase):

    @patch("itential.src.auth.Auth.authenticate")
    def test_create(self, auth_mock: MagicMock) -> None:
        auth_mock.return_value = None  # Skips attempting to authenticate.

        itential2021_1 = Itential.create(version=ItentialVersion.V2021_1)
        # itential2023_1 = Itential.create(version=ItentialVersion.V2023_1)
        # Additional versions

        self.assertIsInstance(itential2021_1, Itential2021_1)
        # self.assertIsInstance(itential2023_1, Itential2023_1)
