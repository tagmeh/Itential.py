import json
import unittest
from datetime import datetime
from unittest.mock import patch

from src.v2021_1.models import JobModel2021_1
from src import create_itential, ItentialVersion

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

        with open(test_path / "mocks/v2021_1/jobs/get_job_by_id.json") as f:
            cls.job_response_json = json.load(f)

    def test_model_creation(self):
        """Simple tests to make sure there are no errors when creating a pydantic job instance."""
        job_instance = JobModel2021_1(itential_instance=self.itential, **self.job_response_json)

        self.assertIsInstance(job_instance, JobModel2021_1)

    def test_datetime_formats(self):
        """
        Tests that the pydantic model JobModel2021_1 outputs the correctly formatted ISO string.
        """
        job_json = self.job_response_json
        job = JobModel2021_1(itential_instance=self.itential, **job_json)

        self.assertIsInstance(job, JobModel2021_1)
        self.assertIsInstance(job.last_updated, datetime)

        deserialized_model = job.model_dump(mode="json")

        # Todo: Test if a default ISO format will work with Itential.
        # Tests that the pydantic model correctly translates the datetime objects into the
        #  Itential-specific ISO format ("2024-12-21T04:26:01.139Z")
        self.assertEqual(
            job_json["last_updated"],
            deserialized_model["last_updated"],
            "The pydantic model should ouput the correct ISO format that Itential expects.",
        )

        # Timestamp should include the microseconds without the period.
        # Itential expects 1734755165218, not what datetime.timestamp() outputs: 1734755165.218
        self.assertEqual(
            job_json["metrics"]["start_time"],
            deserialized_model["metrics"]["start_time"],
            "The pydantic model should output the correct timestamp that Itential expects.",
        )

    def test_property_key_case(self):
        """
        A crude test to make sure the camelCase versions of the Itential
        object are being returned from the pydantic model.
        """
        job_json: dict = self.job_response_json
        job = JobModel2021_1(itential_instance=self.itential, **job_json)

        list_of_camel_case_keys = ["_id", "lastUpdatedVersion", "createdVersion", "canvasVersion", "preAutomationTime"]

        serialized_job = job.model_dump(mode="json")
        serialized_job_keys = serialized_job.keys()

        for key in list_of_camel_case_keys:
            self.assertIn(key, serialized_job_keys)
