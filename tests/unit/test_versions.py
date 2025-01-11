from unittest import TestCase

from src.versions import ItentialVersion


class TestVersions(TestCase):
    def test_version_value_format(self):
        """Validate the values of the ItentialVersion enum are strings."""

        for version in ItentialVersion:
            self.assertIsInstance(version.value, str)
            self.assertIn(".", version.value)

    def test_version_key_format(self):
        """Validate that the keys of the ItentialVersion enum are derived from the string values."""

        for version in ItentialVersion:
            self.assertEqual(version.name, f"V{version.value.replace('.', '_')}")
