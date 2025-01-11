import json
import unittest
from datetime import datetime
from unittest.mock import patch

from src import ItentialVersion, create_itential
from src.v2021_1.models import WorkflowModel2021_1

from tests.mocks.utils import get_test_base_path


class TestJobModel2021_1(unittest.TestCase):

    @classmethod
    @patch("src.base.itential.Itential.authenticate")
    def setUpClass(cls, mock_auth):
        mock_auth.return_value = None
        test_path = get_test_base_path(__file__)

        # TODO: This itential object should be mocked. Couldn't figure out a way of mocking it where Pydantic
        #  didn't complain about the <MagicMock> type of the mocked Itential object.
        cls.itential = create_itential(version=ItentialVersion.V2021_1)

        # 1 Workflow dict, missing _id by design
        with open(test_path / "mocks/v2021_1/workflows/export_workflow.json") as f:
            cls.export_workflow_response_json = json.load(f)

        # 1 Workflow dict wrapped in a list, full workflow object
        with open(test_path / "mocks/v2021_1/workflows/search_workflow.json") as f:
            cls.search_workflow_response_json = json.load(f)

        # Multiple Workflow dicts wrapped in a list, full workflow objects
        with open(test_path / "mocks/v2021_1/workflows/search_workflows.json") as f:
            cls.search_workflows_response_json = json.load(f)

    def test_datetime_format_iso(self):
        """
        Tests that the pydantic model WorkflowModel2021_1 outputs the correctly formatted ISO string.
        """
        workflow_json = self.search_workflow_response_json["results"][0]

        workflow = WorkflowModel2021_1(itential_instance=self.itential, **workflow_json)

        self.assertIsInstance(workflow, WorkflowModel2021_1)
        self.assertIsInstance(workflow.last_updated, datetime)

        deserialized_model = workflow.model_dump(mode="json")

        # Tests that the pydantic model correctly translates the datetime objects into the
        #  Itential-specific ISO format ("2024-12-21T04:26:01.139Z")
        self.assertEqual(workflow_json["last_updated"], deserialized_model["last_updated"])
