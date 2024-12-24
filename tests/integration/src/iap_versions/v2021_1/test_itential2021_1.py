import unittest

from itential import Itential
from itential.src.versions import ItentialVersion

username = ""
password = ""
url = ""


class TestItential2021_1(unittest.TestCase):
    """
    Tests the Itential2021_1 API implementation. Focus tests on the crafted payload and response object.
    The unit tests should have the payload generation and pydantic object non-response properties locked down.
    The integration tests will focus on the payload's effect on the response object.
    """

    @classmethod
    def setUpClass(cls):
        cls.itential2021_1 = Itential.create(version=ItentialVersion.V2021_1)

        # open the test workflow(s)/etc and import them into the platform.
