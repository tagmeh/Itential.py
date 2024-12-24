import json
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from itential import Itential
from itential.src.iap_versions.v2021_1 import Itential2021_1, Job2021_1, Workflow2021_1
from itential.src.versions import ItentialVersion


class TestItential2021_1(unittest.TestCase):
    """
    Tests the Itential2021_1 API implementation. Focus tests on the crafted payload and response object.
    Due to the nature of unit testing a 3rd party API, the API filters don't affect the mock responses.
    For Example:
        If you mock a full job object from the API, but you pass in an 'exclude' filter, the response will still
        contain all the fields and their values.

    The best we can do is test that the payload is crafted correctly and that the response object is the right type
    and contains the library-required fields (e.g. _itential) and its methods work as expected.

    Methods that rely heavily on the 'include'/'exclude' filters will have to be tested in the integration tests.
    """

    @classmethod
    @patch("itential.src.auth.Auth.authenticate")
    def setUpClass(cls, mock_call: MagicMock) -> None:
        # Mock response
        mock_call.return_value = None

        base_path = Path(__file__).parents[4]  # tests/

        cls.itential2021_1 = Itential.create(version=ItentialVersion.V2021_1)

        # 1 Job dict, a full job object
        with open(base_path / "mocks/v2021_1/jobs/get_job_by_id.json") as f:
            cls.get_job_by_id_response_json = json.load(f)

        # 1 dict, a job's job-level variables
        with open(base_path / "mocks/v2021_1/jobs/get_job_output.json") as f:
            cls.get_job_output_response_json = json.load(f)

        # 1 Job dict wrapped in a list, intentionally lacking fields  ('exclude' arg)
        with open(base_path / "mocks/v2021_1/jobs/search_lean_job.json") as f:
            cls.get_lean_job_response_json = json.load(f)

        # Multiple Job dicts wrapped in a list, intentionally lacking fields  ('exclude' arg)
        with open(base_path / "mocks/v2021_1/jobs/search_lean_jobs.json") as f:
            cls.search_lean_jobs_response_json = json.load(f)

        # Multiple job dicts wrapped in a list, full job objects
        with open(base_path / "mocks/v2021_1/jobs/search_jobs.json") as f:
            cls.search_jobs_response_json = json.load(f)

        # 1 Workflow dict, missing _id by design
        with open(base_path / "mocks/v2021_1/workflows/export_workflow.json") as f:
            cls.export_workflow_response_json = json.load(f)

        # 1 Workflow dict wrapped in a list, full workflow object
        with open(base_path / "mocks/v2021_1/workflows/search_workflow.json") as f:
            cls.search_workflow_response_json = json.load(f)

        # Multiple Workflow dicts wrapped in a list, full workflow objects
        with open(base_path / "mocks/v2021_1/workflows/search_workflows.json") as f:
            cls.search_workflows_response_json = json.load(f)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_job(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True  # Required to get the positive response.
        mock_response.json.return_value = self.get_job_by_id_response_json
        mock_call.return_value = mock_response

        expected_endpoint = "/workflow_engine/getJob/bdec683c9d4b4abd879518d9"

        # Call get_job method
        job = self.itential2021_1.get_job(job_id="bdec683c9d4b4abd879518d9")
        _, kwargs = mock_call.call_args  # Get the arguments passed to the call

        # Test Request
        self.assertEqual(kwargs["endpoint"], expected_endpoint)

        # Test Response
        self.assertIsInstance(job, Job2021_1)  # Assert that the job is an instance of Job2021_1
        self.assertEqual(job.id, "bdec683c9d4b4abd879518d9")  # Assert that the job id is captured from "_id"
        self.assertEqual(job.name, "Test Workflow")
        self.assertEqual(job.status, "complete")
        self.assertEqual(job.variables, None)  # Assert that the job variables are not captured in 2021.1
        self.assertIsInstance(job._itential, Itential2021_1)  # Assert that the job has an instance of Itential2021_1

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_job_include(self, mock_call):
        """
        Test the get_lean_job crafts the correct payload when the 'include' parameter is passed.
        """
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.get_lean_job_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"_id": "0752f4ce283b4fe98314f4f7"},
                "limit": 1,
                "skip": 0,
                "expand": ["last_updated_by", "created_by"],
                "sort": {"metrics.start_time": -1},
                "fields": {"status": 1, "createdVersion": 1, "metrics": 1},
            }
        }

        # Call get_lean_job method
        lean_job = self.itential2021_1.get_lean_job(
            job_id="0752f4ce283b4fe98314f4f7", include=["status", "createdVersion", "metrics"]
        )
        _, kwargs = mock_call.call_args  # Get the arguments passed to the call

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload, "The main test is against the 'fields' key.")

        # Test Response
        self.assertIsInstance(lean_job, Job2021_1)
        self.assertEqual(lean_job.id, "0752f4ce283b4fe98314f4f7")
        self.assertIsInstance(lean_job._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_job_exclude(self, mock_call):
        """
        Test the get_lean_job crafts the correct payload when 'exclude' is passed.
        """
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.get_lean_job_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"_id": "0752f4ce283b4fe98314f4f7"},
                "limit": 1,
                "skip": 0,
                "expand": ["last_updated_by", "created_by"],
                "sort": {"metrics.start_time": -1},
                "fields": {
                    "createdVersion": 0,
                    "metrics": 0,
                    "status": 0,
                    "created_by._meta": 0,  # This is an auto-injected field when user uses 'exclude'
                    "created_by.assignedRoles": 0,  # This is an auto-injected field when user uses 'exclude'
                    "created_by.memberOf": 0,  # This is an auto-injected field when user uses 'exclude'
                    "last_updated_by._meta": 0,  # This is an auto-injected field when user uses 'exclude'
                    "last_updated_by.assignedRoles": 0,  # This is an auto-injected field when user uses 'exclude'
                    "last_updated_by.memberOf": 0,  # This is an auto-injected field when user uses 'exclude'
                    "tasks": 0,  # This is an auto-injected field when user uses 'exclude'
                    "transitions": 0,  # This is an auto-injected field when user uses 'exclude'
                },
            }
        }

        # Call get_lean_job method
        lean_job = self.itential2021_1.get_lean_job(
            job_id="0752f4ce283b4fe98314f4f7", exclude=["status", "createdVersion", "metrics"]
        )
        _, kwargs = mock_call.call_args  # Get the arguments passed to the call

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(lean_job, Job2021_1)
        self.assertEqual(lean_job.id, "0752f4ce283b4fe98314f4f7")  # _id is always returned unless explicitly excluded
        self.assertIsInstance(lean_job._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_job_neither_include_nor_exclude(self, mock_call):
        """
        Test the get_lean_job crafts the correct payload when 'exclude' is passed.
        """
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.get_lean_job_response_json
        mock_call.return_value = mock_response

        with self.assertRaises(ValueError) as error:
            _ = self.itential2021_1.get_lean_job(job_id="0752f4ce283b4fe98314f4f7")

        self.assertEqual(str(error.exception), "Either 'include' or 'exclude' arg must be provided.")

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_job_neither_include_and_exclude(self, mock_call):
        """
        Test the get_lean_job crafts the correct payload when 'exclude' is passed.
        """
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.get_lean_job_response_json
        mock_call.return_value = mock_response

        with self.assertRaises(ValueError) as error:
            _ = self.itential2021_1.get_lean_job(
                job_id="0752f4ce283b4fe98314f4f7", include=["status"], exclude=["not_status"]
            )

        self.assertEqual(str(error.exception), "Either 'include' OR 'exclude' arg must be provided, not both.")

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_job_output_using_job_object(self, mock_call):
        """
        Test the get_job_output method using a Job object.
        """
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.get_job_output_response_json
        mock_call.return_value = mock_response

        # Create a Job object
        job = Job2021_1(**{"_itential": self.itential2021_1}, **self.get_job_by_id_response_json)

        # Call get_job_output method
        job = self.itential2021_1.get_job_output(job=job)

        # Validate the job output is correctly applied to the variables attribute.
        self.assertEqual(job.variables, self.get_job_output_response_json)
        self.assertIsInstance(job, Job2021_1)
        self.assertIsInstance(job._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_job_output_using_job_id_string(self, mock_call):
        """
        Test the get_job_output method using a Job object.
        """
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.get_job_output_response_json
        mock_call.return_value = mock_response

        dynamic_job_id: str = self.get_job_output_response_json["_id"]

        # Call get_job_output method
        job = self.itential2021_1.get_job_output(job_id=dynamic_job_id)

        # Validate the job output is correctly applied to the variables attribute.
        self.assertEqual(job.variables, self.get_job_output_response_json)
        self.assertIsInstance(job, Job2021_1)
        self.assertIsInstance(job._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_jobs_by_workflow_name(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_jobs_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow"},
                # Everything below this point are defaults
                "limit": 100,
                "skip": 0,
                "expand": ["last_updated_by", "created_by"],
                "sort": {"metrics.start_time": -1},
                "fields": {
                    "created_by._meta": 0,
                    "created_by.assignedRoles": 0,
                    "created_by.memberOf": 0,
                    "last_updated_by._meta": 0,
                    "last_updated_by.assignedRoles": 0,
                    "last_updated_by.memberOf": 0,
                    "tasks": 0,
                    "transitions": 0,
                },
            }
        }

        # Call get_jobs method
        jobs = self.itential2021_1.get_jobs(workflow_name="Test Workflow")
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(jobs, list)
        self.assertIsInstance(jobs[0], Job2021_1)
        self.assertEqual(jobs[0].name, "Test Workflow")
        self.assertIsInstance(jobs[0]._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_jobs_by_query(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_jobs_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow", "status": "complete"},
                "limit": 50,
                "skip": 1,
                "expand": ["last_updated_by", "created_by"],
                "sort": {"metrics.start_time": 1},
                "fields": {"tasks": 1, "transitions": 1},
            }
        }

        # Call get_jobs method
        jobs = self.itential2021_1.get_jobs(
            query={"name": "Test Workflow", "status": "complete"},
            limit=50,
            skip=1,
            sort={"metrics.start_time": 1},
            fields={"tasks": 1, "transitions": 1},
        )
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(jobs, list)
        self.assertIsInstance(jobs[0], Job2021_1)
        self.assertEqual(jobs[0].name, "Test Workflow")
        self.assertIsInstance(jobs[0]._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_jobs_by_workflow_name_include(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_lean_jobs_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow"},
                "limit": 100,
                "skip": 0,
                "sort": {"metrics.start_time": -1},
                "fields": {"status": 1, "createdVersion": 1, "metrics": 1},
            }
        }

        # Call get_lean_jobs method
        lean_jobs = self.itential2021_1.get_lean_jobs(
            workflow_name="Test Workflow", include=["status", "createdVersion", "metrics"]
        )
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(lean_jobs, list)
        self.assertIsInstance(lean_jobs[0], Job2021_1)
        self.assertEqual(lean_jobs[0].name, None)
        self.assertEqual(lean_jobs[0].status, "complete")
        self.assertEqual(lean_jobs[0].last_updated_by, None)
        self.assertEqual(lean_jobs[0].variables, None)
        self.assertIsInstance(lean_jobs[0]._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_jobs_by_workflow_name_exclude(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_lean_jobs_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow"},
                "limit": 100,
                "skip": 0,
                "sort": {"metrics.start_time": -1},
                "fields": {
                    "ancestors": 0,
                    "decorators": 0,
                    "description": 0,
                    "tasks": 0,
                    "transitions": 0,
                },
            }
        }

        # Call get_lean_jobs method
        lean_jobs = self.itential2021_1.get_lean_jobs(
            workflow_name="Test Workflow", exclude=["description", "decorators", "ancestors"]
        )
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(lean_jobs, list)
        self.assertIsInstance(lean_jobs[0], Job2021_1)
        self.assertEqual(lean_jobs[0].description, None)
        self.assertEqual(lean_jobs[0].decorators, None)
        self.assertEqual(lean_jobs[0].ancestors, None)
        self.assertEqual(lean_jobs[0].variables, None)
        self.assertIsInstance(lean_jobs[0]._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_jobs_neither_include_nor_exclude(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_lean_jobs_response_json
        mock_call.return_value = mock_response

        with self.assertRaises(ValueError) as error:
            _ = self.itential2021_1.get_lean_jobs(workflow_name="Test Workflow")

        self.assertEqual(str(error.exception), "Either 'include' or 'exclude' arg must be provided.")

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_jobs_neither_include_and_exclude(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_lean_jobs_response_json
        mock_call.return_value = mock_response

        with self.assertRaises(ValueError) as error:
            _ = self.itential2021_1.get_lean_jobs(
                workflow_name="Test Workflow", include=["status"], exclude=["not_status"]
            )

        self.assertEqual(str(error.exception), "Either 'include' OR 'exclude' arg must be provided, not both.")

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
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
        workflow = self.itential2021_1.get_workflow(workflow_name="Test Workflow")
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflow, Workflow2021_1)
        self.assertEqual(workflow.name, "Test Workflow")
        self.assertIsInstance(workflow._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
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
        workflow = self.itential2021_1.get_workflow(query={"name": "Test Workflow", "status": "complete"})
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflow, Workflow2021_1)
        self.assertEqual(workflow.name, "Test Workflow")
        self.assertIsInstance(workflow._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
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
                    "name": 1,  # This field is auto-injected if using 'include' when calling get_lean_workflow(workflow_name=)
                },
            }
        }

        # Call get_lean_workflow method
        lean_workflow = self.itential2021_1.get_lean_workflow(
            workflow_name="Test Workflow", include=["type", "last_updated_by", "inputSchema"]
        )
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(lean_workflow, Workflow2021_1)
        self.assertEqual(lean_workflow.name, "Test Workflow")
        self.assertEqual(lean_workflow.last_updated_by, "675c936a13675f000b815be4")
        self.assertIsInstance(lean_workflow._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
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
        workflows = self.itential2021_1.get_workflows(workflow_name="Test Workflow")
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflows, list)
        self.assertIsInstance(workflows[0], Workflow2021_1)
        self.assertEqual(workflows[0].name, "Test Workflow")
        self.assertIsInstance(workflows[0]._itential, Itential2021_1)

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
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
        workflows = self.itential2021_1.get_workflows(
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
        self.assertIsInstance(workflows[0], Workflow2021_1, "The object in the list should be a Workflow2021_1 object.")
        self.assertIsInstance(
            workflows[0]._itential, Itential2021_1, "The workflow object should have an instance of Itential2021_1."
        )
        self.assertEqual(workflows[0].name, "Test Workflow", "The pydantic model should have stored the workflow name.")

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
    def test_export_workflow(self, mock_call):
        """
        Itential.export_workflow is only called by "workflow_name", since the workflow name is unique within the platform.
        """

        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.export_workflow_response_json
        mock_call.return_value = mock_response

        expected_payload = {"options": {"name": "Test Workflow", "type": "automation"}}

        # Call export_workflow method
        workflow = self.itential2021_1.export_workflow(workflow_name="Test Workflow")
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflow, Workflow2021_1)
        self.assertIsInstance(workflow._itential, Itential2021_1)
        self.assertEqual(workflow.name, "Test Workflow")
        self.assertEqual(workflow.id, None, "The id is not returned in the export_workflow response.")
        self.assertEqual(workflow.errors, None, "The errors are not returned in the export_workflow response.")

    @patch("itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1.call")
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

        job = Job2021_1(**{"_itential": self.itential2021_1}, **self.get_job_by_id_response_json)

        # Call get_workflow method
        workflow = self.itential2021_1.get_workflow(job=job)
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(workflow, Workflow2021_1)
        self.assertEqual(workflow.name, "Test Workflow")
        self.assertIsInstance(workflow._itential, Itential2021_1)


if __name__ == "__main__":
    unittest.main()
