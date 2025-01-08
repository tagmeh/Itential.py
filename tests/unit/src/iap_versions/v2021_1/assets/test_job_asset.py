import json
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from itential import Itential
from itential.src.iap_versions.v2021_1 import Itential2021_1
from itential.src.iap_versions.v2021_1.models.job2021_1 import Job2021_1
from itential.src.iap_versions.v2021_1.models.workflow2021_1 import Workflow2021_1
from itential.src.versions import ItentialVersion


class TestItential2021_1(unittest.TestCase):
    """
    Tests the Itential2021_1 API implementation. Focus tests on the crafted payload and response object.
    Due to the nature of unit testing a 3rd party API, the API filters don't affect the mock responses.
    For Example:
        If you mock a full job object from the API, but you pass in an 'exclude' filter, the response will still
        contain all the fields and their values.

    The best we can do is test that the payload is crafted correctly and that the response object is the right type
    and contains the library-required fields (e.g. itential_instance) and its methods work as expected.

    Methods that rely heavily on the 'include'/'exclude' filters will have to be tested in the integration tests.
    """

    @classmethod
    @patch("itential.src.auth.Auth.authenticate")
    def setUpClass(cls, mock_call: MagicMock) -> None:
        # Mock response
        mock_call.return_value = None

        base_path = Path(__file__).parents[5]  # tests/

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
