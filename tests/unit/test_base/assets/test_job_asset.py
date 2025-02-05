import unittest

from src.base import JobAsset
from tests.mocks.utils import concreter


class TestJobAsset(unittest.TestCase):
    """
    Tests for the JobAsset abstract class.

    Not entirely sure what or how to test this class.
    """

    @classmethod
    def setUpClass(self):
        self.concrete_job_asset = concreter(JobAsset)  # Concrete Abstract class

    def test_concrete_job_asset_methods(self):
        """Validate the JobAsset Class contains the required methods"""

        expected_methods = ["retrieve", "retrieve_lean", "search", "search_lean", "output"].sort()
        concrete_methods = [method for method in self.concrete_job_asset.__dict__ if not method.startswith("__")].sort()

        self.assertEqual(expected_methods, concrete_methods)


if __name__ == "__main__":
    unittest.main()
