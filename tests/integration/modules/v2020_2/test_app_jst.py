import time
import unittest

from itential.core import Itential
from itential.modules.v2020_2 import AppJst
from tests.integration.mocks.v2020_2.app_jst import jst_json

unittest.TestLoader.sortTestMethodsUsing = None


class AppJstTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = Itential()  # Testing with the current local server

    def test_create_transformation_success(self):
        """
        Create a JST/Transformation in Itential
        Then remove the JST/Transformation
        """
        response = AppJst.create_transformation(client=self.client, jst_obj=jst_json)

        content = response.json()

        time.sleep(1)
        AppJst.delete_transformation(client=self.client, jst_id=content['_id'])  # Clean up

        # Assume this call will succeed
        self.assertEqual(response.status_code, 200)
        # Simple json value check
        self.assertEqual(content['name'], "TestJST")

    def test_create_transformation_failure(self):
        """
        Create a JST/Transformation
        Try to create the same JST/Transformation
        Then remove the JST/Transformation
        """
        AppJst.create_transformation(client=self.client, jst_obj=jst_json)  # To create the JST
        response = AppJst.create_transformation(client=self.client, jst_obj=jst_json)  # To error out
        time.sleep(1)
        AppJst.delete_transformation(client=self.client, jst_id=response.json().get('_id'))  # Clean up

        content = response.json()

        self.assertEqual(content['apiVersion'], "1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['error']['message'], "Transformation with given name already exists")
