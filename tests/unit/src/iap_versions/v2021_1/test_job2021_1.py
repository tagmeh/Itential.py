import json
import unittest
from datetime import datetime
from pathlib import Path

from itential.src.iap_versions.v2021_1 import Job2021_1


class Testjob2021_1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base_path = Path(__file__).parents[4]  # tests/

        with open(base_path / "mocks/v2021_1/jobs/get_job_by_id.json", "r") as f:
            cls.job_response_json = json.load(f)

    def test_model_creation(self):
        """ Simple tests to make sure there are no errors when creating a pydantic job instance. """
        job_instance = Job2021_1(**self.job_response_json)

        self.assertIsInstance(job_instance, Job2021_1)

    def test_datetime_formats(self):
        """
        Tests that the pydantic model Job2021_1 outputs the correctly formatted ISO string.
        """
        job_json = self.job_response_json
        job = Job2021_1(**job_json)

        self.assertIsInstance(job, Job2021_1)
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
        job = Job2021_1(**job_json)

        list_of_camel_case_keys = ["_id", "lastUpdatedVersion", "createdVersion", "canvasVersion", "preAutomationTime"]

        serialized_job = job.model_dump(mode="json", by_alias=True)
        serialized_job_keys = serialized_job.keys()

        for key in list_of_camel_case_keys:
            self.assertIn(key, serialized_job_keys)
