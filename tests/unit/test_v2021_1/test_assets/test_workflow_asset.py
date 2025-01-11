import json
import unittest
from unittest.mock import MagicMock, patch

from src.v2021_1 import Itential2021_1
from src.v2021_1.models.workflow_model import WorkflowModel2021_1
from src.v2021_1.models.job_model import JobModel2021_1
from tests.mocks.utils import get_test_base_path


class TestWorkflowModel2021_1(unittest.TestCase):

    @classmethod
    @patch("src.v2021_1.itential2021_1.Itential2021_1.authenticate")
    def setUpClass(cls, mock_auth):
        mock_response = MagicMock()
        mock_response.json.return_value = None

        cls.maxDiff = None

        test_path = get_test_base_path(__file__)

        cls.itential2021_1 = Itential2021_1("", "", "")

        # 1 Job dict, a full job object
        with open(test_path / "mocks/v2021_1/jobs/get_job_by_id.json") as f:
            cls.get_job_by_id_response_json = json.load(f)

        # 1 Workflow dict, missing _id by design
        with open(test_path / "mocks/v2021_1/workflows/export_workflow.json") as f:
            cls.export_workflow_response_json = json.load(f)

        # 1 Workflow dict wrapped in a list, full workflow object
        with open(test_path / "mocks/v2021_1/workflows/search_workflow.json") as f:
            cls.search_workflow_response_json = json.load(f)

        # Multiple Workflow dicts wrapped in a list, full workflow objects
        with open(test_path / "mocks/v2021_1/workflows/search_workflows.json") as f:
            cls.search_workflows_response_json = json.load(f)

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_workflow_by_workflow_name(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_workflow_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow"},
                # Default params.
                "limit": 1,  # hard-coded limit.
                "skip": 0,  # hard-coded skip.
                "expand": ["last_updated_by", "created_by"],
                "fields": {
                    "tasks": 0,
                    "transitions": 0,
                    "last_updated_by.memberOf": 0,
                    "last_updated_by.assignedRoles": 0,
                    "last_updated_by._meta": 0,
                    "created_by.memberOf": 0,
                    "created_by.assignedRoles": 0,
                    "created_by._meta": 0,
                },
            }
        }

        # Call get_workflow method
        workflow = self.itential2021_1.workflow.retrieve(workflow_name="Test Workflow")
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflow, WorkflowModel2021_1)
        self.assertEqual(workflow.name, "Test Workflow")
        self.assertIsInstance(workflow.itential_instance, Itential2021_1, type(workflow.itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_workflow_by_query(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_workflow_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow", "status": "complete"},
                # Default params
                "limit": 1,  # hard-coded limit.
                "skip": 0,  # hard-coded skip.
                "expand": ["last_updated_by", "created_by"],
                "fields": {
                    "tasks": 0,
                    "transitions": 0,
                    "last_updated_by.memberOf": 0,
                    "last_updated_by.assignedRoles": 0,
                    "last_updated_by._meta": 0,
                    "created_by.memberOf": 0,
                    "created_by.assignedRoles": 0,
                    "created_by._meta": 0,
                },
            }
        }

        # Call get_workflow method
        workflow = self.itential2021_1.workflow.retrieve(query={"name": "Test Workflow", "status": "complete"})
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflow, WorkflowModel2021_1)
        self.assertEqual(workflow.name, "Test Workflow")
        self.assertIsInstance(workflow.itential_instance, Itential2021_1)

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_workflow_by_workflow_name_include(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_workflow_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow"},
                "limit": 1,
                "skip": 0,
                "fields": {
                    "type": 1,
                    "last_updated_by": 1,
                    "inputSchema": 1,
                    "name": 1,  # This field is auto-injected if using 'include' when calling
                    # workflow.retrieve_lean(workflow_name=)
                },
            }
        }

        # Call get_lean_workflow method
        lean_workflow = self.itential2021_1.workflow.retrieve_lean(
            workflow_name="Test Workflow", include=["type", "last_updated_by", "inputSchema"]
        )
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(lean_workflow, WorkflowModel2021_1)
        self.assertEqual(lean_workflow.name, "Test Workflow")
        self.assertEqual(lean_workflow.last_updated_by, "675c936a13675f000b815be4")
        self.assertIsInstance(lean_workflow.itential_instance, Itential2021_1)

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_workflows_by_workflow_name(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_workflows_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow"},
                "limit": 100,  # server-enforced maximum.
                "skip": 0,
                "expand": ["last_updated_by", "created_by"],
                "sort": {"metrics.start_time": -1},
                "fields": {
                    "tasks": 0,
                    "transitions": 0,
                    "last_updated_by.memberOf": 0,
                    "last_updated_by.assignedRoles": 0,
                    "last_updated_by._meta": 0,
                    "created_by.memberOf": 0,
                    "created_by.assignedRoles": 0,
                    "created_by._meta": 0,
                },
            }
        }

        # Call get_workflows method
        workflows = self.itential2021_1.workflow.search(workflow_name="Test Workflow")
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflows, list)
        self.assertIsInstance(workflows[0], WorkflowModel2021_1)
        self.assertEqual(workflows[0].name, "Test Workflow")
        self.assertIsInstance(workflows[0].itential_instance, Itential2021_1, type(workflows[0].itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_workflows_by_query(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_workflows_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow"},
                "limit": 50,
                "skip": 0,  # Default
                "expand": ["last_updated_by", "created_by"],  # Default
                "sort": {"metrics.start_time": 1},  # Default
                "fields": {
                    "tasks": 0,
                    "transitions": 0,
                    "last_updated_by.memberOf": 0,
                    "last_updated_by.assignedRoles": 0,
                    "last_updated_by._meta": 0,
                    "created_by.memberOf": 0,
                    "created_by.assignedRoles": 0,
                    "created_by._meta": 0,
                },  # Default
            }
        }

        # Call get_workflows method
        workflows = self.itential2021_1.workflow.search(
            query={"name": "Test Workflow"},
            get_all=False,
            max_amt=0,
            limit=50,
            skip=0,
            sort={"metrics.start_time": 1},
            fields={
                "tasks": 0,
                "transitions": 0,
                "last_updated_by.memberOf": 0,
                "last_updated_by.assignedRoles": 0,
                "last_updated_by._meta": 0,
                "created_by.memberOf": 0,
                "created_by.assignedRoles": 0,
                "created_by._meta": 0,
            },
        )

        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflows, list)
        self.assertIsInstance(
            workflows[0], WorkflowModel2021_1, "The object in the list should be a WorkflowModel2021_1 object."
        )
        self.assertIsInstance(
            workflows[0].itential_instance,
            Itential2021_1,
            "The workflow object should have an instance of Itential2021_1.",
        )
        self.assertEqual(workflows[0].name, "Test Workflow", "The pydantic model should have stored the workflow name.")

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_export_workflow(self, mock_call):
        """
        Itential.export_workflow is only called by "workflow_name", since the workflow name is unique within the
        platform.
        """

        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.export_workflow_response_json
        mock_call.return_value = mock_response

        expected_payload = {"options": {"name": "Test Workflow", "type": "automation"}}

        # Call export_workflow method
        workflow = self.itential2021_1.workflow.export(workflow_name="Test Workflow")
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflow, WorkflowModel2021_1)
        self.assertIsInstance(workflow.itential_instance, Itential2021_1)
        self.assertEqual(workflow.name, "Test Workflow")
        self.assertEqual(workflow.id, None, "The id is not returned in the export_workflow response.")
        self.assertEqual(workflow.errors, None, "The errors are not returned in the export_workflow response.")

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_workflow_by_job(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_workflow_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow"},
                "limit": 1,
                "skip": 0,
                "expand": ["last_updated_by", "created_by"],
                "fields": {
                    "tasks": 0,
                    "transitions": 0,
                    "last_updated_by.memberOf": 0,
                    "last_updated_by.assignedRoles": 0,
                    "last_updated_by._meta": 0,
                    "created_by.memberOf": 0,
                    "created_by.assignedRoles": 0,
                    "created_by._meta": 0,
                },
            }
        }

        job = JobModel2021_1(**{"itential_instance": self.itential2021_1}, **self.get_job_by_id_response_json)

        # Call get_workflow method
        workflow = self.itential2021_1.workflow.retrieve(job=job)
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflow, WorkflowModel2021_1)
        self.assertEqual(workflow.name, "Test Workflow")
        self.assertIsInstance(workflow.itential_instance, Itential2021_1)
