from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from itential.src.iap_versions.base import Job
from itential.src.versions import ItentialVersion


class JobParent(BaseModel):
    job: str | None = None
    task: str | None = None
    iteration: int | None = None
    element: int | None = None


class JobMetrics(BaseModel):
    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.timestamp() * 1000}

    start_time: datetime | None = None
    user: str | None = None
    progress: int | float | None = None
    end_time: datetime | None = None  # A Job that is not yet completed will not have an "end_time" field.


class JobError(BaseModel):
    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.timestamp() * 1000}

    message: str | None = None
    task: str | None = None
    timestamp: datetime | None = None


class Job2021_1(Job):
    """Describes a job in the 2021.1 version of the Itential API"""

    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}

    _version: ItentialVersion = ItentialVersion.V2021_1
    id: str | None = Field(alias="_id", default=None)
    name: str | None = None
    description: str | None = None
    tasks: dict[str, dict[str, Any]] | str = "Use 'Job.update()' to get tasks."
    transitions: dict[str, dict[str, Any]] | str = "Use 'Job.update()' to get transitions."
    last_updated: datetime | None = None
    last_updated_by: str | None = None
    last_updated_version: str | None = Field(alias="lastUpdatedVersion", default=None)
    created: datetime | None = None
    created_by: str | None = None
    created_version: str | None = Field(alias="createdVersion", default=None)
    canvas_version: int | None = Field(alias="canvasVersion", default=None)
    pre_automation_time: int | None = Field(alias="preAutomationTime", default=None)
    sla: int | None = None
    groups: list[str] | None = None
    status: str | None = None
    variables: dict[str, Any] | None = None
    watchers: list[str] | None = None
    ancestors: list[str] | None = None
    parent: JobParent | None = None
    decorators: list[str] | None = None
    metrics: JobMetrics | None = None
    error: list[JobError] | None = None

    def get_output(self) -> "Job2021_1":
        """
        Gets the output of the Job if possible.
        Cannot get output from a job that is not in "complete" status
        Updates self and returns self, for chaining purposes.
        """
        if self.status not in ["complete"]:
            print(f"Cannot get job '{self.id}' output for job that is not in 'complete' status. ({self.status})")
            return self

        job = self.itential.get_job_output(job=self.id)
        self.__dict__.update(job.__dict__)
        return self

    def update(self) -> "Job2021_1":
        """Itential 2021.1 doesn't return the job output by default, so we extend the update method."""
        super().update()
        self.get_output()
        return self
