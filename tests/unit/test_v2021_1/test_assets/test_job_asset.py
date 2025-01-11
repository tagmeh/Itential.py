import json
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from src import create_itential, ItentialVersion
from src.exceptions import ApiError
from src.v2021_1 import Itential2021_1
from src.v2021_1.assets.job_asset import JobAsset2021_1
from src.v2021_1.models import JobModel2021_1
from tests.mocks.utils import get_test_base_path


class TestJobAsset2021_1(unittest.TestCase):

    @classmethod
    @patch("src.base.itential.Itential.authenticate")
    def setUpClass(cls, mock_call: MagicMock) -> None:
        # Mock response
        mock_call.return_value = None

        test_path = get_test_base_path(__file__)

        cls.itential2021_1 = create_itential(version=ItentialVersion.V2021_1)

        cls.job_asset = cls.itential2021_1.job

        # 1 Job dict, a full job object
        with open(test_path / "mocks/v2021_1/jobs/get_job_by_id.json") as f:
            cls.get_job_by_id_response_json = json.load(f)

        # 1 dict, a job's job-level variables
        with open(test_path / "mocks/v2021_1/jobs/get_job_output.json") as f:
            cls.get_job_output_response_json = json.load(f)

        # 1 Job dict wrapped in a list, intentionally lacking fields  ('exclude' arg)
        with open(test_path / "mocks/v2021_1/jobs/search_lean_job.json") as f:
            cls.get_lean_job_response_json = json.load(f)

        # Multiple Job dicts wrapped in a list, intentionally lacking fields  ('exclude' arg)
        with open(test_path / "mocks/v2021_1/jobs/search_lean_jobs.json") as f:
            cls.search_lean_jobs_response_json = json.load(f)

        # Multiple job dicts wrapped in a list, full job objects
        with open(test_path / "mocks/v2021_1/jobs/search_jobs.json") as f:
            cls.search_jobs_response_json = json.load(f)

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_job_success(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True  # Required to get the positive response.
        mock_response.json.return_value = self.get_job_by_id_response_json
        mock_call.return_value = mock_response

        expected_endpoint = "/workflow_engine/getJob/bdec683c9d4b4abd879518d9"

        # Call get_job method
        job = self.itential2021_1.job.retrieve(job_id="bdec683c9d4b4abd879518d9")
        _, kwargs = mock_call.call_args  # Get the arguments passed to the call

        # Test Request
        self.assertEqual(kwargs["endpoint"], expected_endpoint)

        # Test Response
        self.assertIsInstance(job, JobModel2021_1)  # Assert that the job is an instance of Job2021_1
        self.assertEqual(job.id, "bdec683c9d4b4abd879518d9")  # Assert that the job id is captured from "_id"
        self.assertEqual(job.name, "Test Workflow")
        self.assertEqual(job.status, "complete")
        self.assertEqual(job.variables, None)  # Assert that the job variables are not captured in 2021.1
        self.assertIsInstance(
            job.itential_instance, Itential2021_1
        )  # Assert that the job has an instance of Itential2021_1

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_job_exception(self, mock_call):

        # Mock response
        mock_response = MagicMock()
        mock_response.ok = False  # Manually trigger the else: raise ApiError branch.
        mock_call.return_value = mock_response

        with self.assertRaises(ApiError):
            self.itential2021_1.job.retrieve(job_id="doesnt_matter")

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
        lean_job = self.itential2021_1.job.retrieve_lean(
            job_id="0752f4ce283b4fe98314f4f7", include=["status", "createdVersion", "metrics"]
        )
        _, kwargs = mock_call.call_args  # Get the arguments passed to the call

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload, "The main test is against the 'fields' key.")

        # Test Response
        self.assertIsInstance(lean_job, JobModel2021_1)
        self.assertEqual(lean_job.id, "0752f4ce283b4fe98314f4f7")
        self.assertIsInstance(lean_job.itential_instance, Itential2021_1, type(lean_job.itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
        lean_job = self.itential2021_1.job.retrieve_lean(
            job_id="0752f4ce283b4fe98314f4f7", exclude=["status", "createdVersion", "metrics"]
        )
        _, kwargs = mock_call.call_args  # Get the arguments passed to the call

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(lean_job, JobModel2021_1)
        self.assertEqual(lean_job.id, "0752f4ce283b4fe98314f4f7")  # _id is always returned unless explicitly excluded
        self.assertIsInstance(lean_job.itential_instance, Itential2021_1, type(lean_job.itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
            _ = self.itential2021_1.job.retrieve_lean(job_id="0752f4ce283b4fe98314f4f7")

        self.assertEqual(str(error.exception), "Either 'include' or 'exclude' arg must be provided.")

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
            _ = self.itential2021_1.job.retrieve_lean(
                job_id="0752f4ce283b4fe98314f4f7", include=["status"], exclude=["not_status"]
            )

        self.assertEqual(str(error.exception), "Either 'include' OR 'exclude' arg must be provided, not both.")

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
        job = JobModel2021_1(**{"itential_instance": self.itential2021_1}, **self.get_job_by_id_response_json)

        # Call get_job_output method
        job = self.itential2021_1.job.output(job=job)

        # Validate the job output is correctly applied to the variables attribute.
        self.assertEqual(job.variables, self.get_job_output_response_json)
        self.assertIsInstance(job, JobModel2021_1)
        self.assertIsInstance(job.itential_instance, Itential2021_1)

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
        job = self.itential2021_1.job.output(job=dynamic_job_id)

        # Validate the job output is correctly applied to the variables attribute.
        self.assertEqual(job.variables, self.get_job_output_response_json)
        self.assertIsInstance(job, JobModel2021_1)
        self.assertIsInstance(job.itential_instance, Itential2021_1, type(job.itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
        jobs = self.itential2021_1.job.search(workflow_name="Test Workflow")
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(jobs, list)
        self.assertIsInstance(jobs[0], JobModel2021_1)
        self.assertEqual(jobs[0].name, "Test Workflow")
        self.assertIsInstance(jobs[0].itential_instance, Itential2021_1, type(jobs[0].itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_jobs_get_all_true(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_jobs_response_json
        mock_call.return_value = mock_response

        expected_payload = {
            "options": {
                "query": {"name": "Test Workflow"},
                "get_all": True,
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
        jobs = self.itential2021_1.job.search(workflow_name="Test Workflow", get_all=True)
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(jobs, list)
        self.assertIsInstance(jobs[0], JobModel2021_1)
        self.assertEqual(jobs[0].name, "Test Workflow")
        self.assertIsInstance(jobs[0].itential_instance, Itential2021_1, type(jobs[0].itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
        jobs = self.itential2021_1.job.search(
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
        self.assertIsInstance(jobs[0], JobModel2021_1)
        self.assertEqual(jobs[0].name, "Test Workflow")
        self.assertIsInstance(jobs[0].itential_instance, Itential2021_1, type(jobs[0].itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
        lean_jobs = self.itential2021_1.job.search_lean(
            workflow_name="Test Workflow", include=["status", "createdVersion", "metrics"]
        )
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(lean_jobs, list)
        self.assertIsInstance(lean_jobs[0], JobModel2021_1)
        self.assertEqual(lean_jobs[0].name, None)
        self.assertEqual(lean_jobs[0].status, "complete")
        self.assertEqual(lean_jobs[0].last_updated_by, None)
        self.assertEqual(lean_jobs[0].variables, None)
        self.assertIsInstance(lean_jobs[0].itential_instance, Itential2021_1, type(lean_jobs[0].itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
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
        lean_jobs = self.itential2021_1.job.search_lean(
            workflow_name="Test Workflow", exclude=["description", "decorators", "ancestors"]
        )
        _, kwargs = mock_call.call_args

        # Test Request
        self.assertEqual(kwargs["json"], expected_payload)

        # Test Response
        self.assertIsInstance(lean_jobs, list)
        self.assertIsInstance(lean_jobs[0], JobModel2021_1)
        self.assertEqual(lean_jobs[0].description, None)
        self.assertEqual(lean_jobs[0].decorators, None)
        self.assertEqual(lean_jobs[0].ancestors, None)
        self.assertEqual(lean_jobs[0].variables, None)
        self.assertIsInstance(lean_jobs[0].itential_instance, Itential2021_1, type(lean_jobs[0].itential_instance))

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_jobs_neither_include_nor_exclude(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_lean_jobs_response_json
        mock_call.return_value = mock_response

        with self.assertRaises(ValueError) as error:
            _ = self.itential2021_1.job.search_lean(workflow_name="Test Workflow")

        self.assertEqual(str(error.exception), "Either 'include' or 'exclude' arg must be provided.")

    @patch("src.v2021_1.itential2021_1.Itential2021_1.call")
    def test_get_lean_jobs_neither_include_and_exclude(self, mock_call):
        # Mock response
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = self.search_lean_jobs_response_json
        mock_call.return_value = mock_response

        with self.assertRaises(ValueError) as error:
            _ = self.itential2021_1.job.search_lean(
                workflow_name="Test Workflow", include=["status"], exclude=["not_status"]
            )

        self.assertEqual(str(error.exception), "Either 'include' OR 'exclude' arg must be provided, not both.")
