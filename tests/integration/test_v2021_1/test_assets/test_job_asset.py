import logging
from unittest import TestCase

from src import create_itential, ItentialVersion

log = logging.getLogger(__name__)


class TestJobAsset2021_1(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.itential = create_itential(version=ItentialVersion.V2021_1)
        log.info("TestJobAsset2021_1 - Itential Instance Created Successfully.")

    def test_search_jobs_get_all(self):
        """
        Blank Job search, should find all jobs on the server.
        Tests the looping logic triggered by the get_all=True parameter.

        (Test written before any automatic server seeding)
        Integration test assumes more than 2 jobs exist on the server.
        Limit set low to avoid having to generate a lot of jobs.
        """
        jobs = self.itential.job.search(query={}, get_all=True, limit=2)

        self.assertIsInstance(jobs, list)
        self.assertGreater(len(jobs), 2, "Make sure there are more than 2 jobs on the server.")
