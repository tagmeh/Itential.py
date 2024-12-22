import json
import unittest
from datetime import datetime
from pathlib import Path

from itential.src.iap_versions.v2021_1 import Workflow2021_1


class TestWorkflow2021_1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base_path = Path(__file__).parents[4]  # tests/

        # 1 Workflow dict wrapped in a list, full workflow object
        with open(base_path / "mocks/v2021_1/workflows/search_workflow.json", 'r') as f:
            cls.search_workflow_response_json = json.load(f)

    def test_datetime_format_iso(self):
        """
        Tests that the pydantic model Workflow2021_1 outputs the correctly formatted ISO string.
        """
        workflow_json = self.search_workflow_response_json['results'][0]
        workflow = Workflow2021_1(**workflow_json)

        self.assertIsInstance(workflow, Workflow2021_1)
        self.assertIsInstance(workflow.last_updated, datetime)

        deserialized_model = workflow.model_dump(mode='json')

        # Tests that the pydantic model correctly translates the datetime objects into the
        #  Itential-specific ISO format ("2024-12-21T04:26:01.139Z")
        self.assertEqual(workflow_json['last_updated'], deserialized_model['last_updated'])
