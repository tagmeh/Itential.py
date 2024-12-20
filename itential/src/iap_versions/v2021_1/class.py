import logging
from typing import overload, Type

from itential import Itential
from itential.src.auth import AuthBase
from itential.src.versions import ItentialVersion

log = logging.getLogger(__name__)


class Itential2021_1(Itential, AuthBase):
    version = ItentialVersion.V2021_1

    def __init__(self, *args, **kwargs):
        super().__init__(self)
        AuthBase.__init__(self, **kwargs)

    def get_jobs(self):
        ...

    def get_jobs_by_workflow_name(self, workflow_name: str):
        ...

    def get_job(self):
        ...

    def get_job_output(self, job_id: str):
        ...

    def get_lean_job(self):
        ...

    def get_job_by_id(self, job_id: str):
        ...

    def get_workflow(self, workflow_name: str):
        ...

    def get_workflows(self, workflow_names: list[str]):
        ...

    def export_workflow(self, workflow_name: str):
        ...

    @overload
    def get_workflow_by_job(self, job_id: str): ...

    @overload
    def get_workflow_by_job(self, job): ...

    def get_workflow_by_job(self, **kwargs):
        job_id = kwargs.get('job_id')
        if job := kwargs.get('job'):
            job_id = job.id

        return job_id

