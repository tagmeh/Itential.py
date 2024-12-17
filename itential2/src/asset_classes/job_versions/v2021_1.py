from datetime import datetime

from pydantic.dataclasses import dataclass

from itential2.src.versions import SupportedVersion
from itential2.src.asset_classes.job_versions.base import Job


@dataclass
class Parent:
    job: str
    task: str
    iteration: int
    element: int
    

@dataclass
class Metrics:
    start_time: int
    user: str
    progress: int
    end_time: int


class Jobv2021_1(Job):
    _version: SupportedVersion = SupportedVersion.V2021_1
    _id: str
    name: str
    description: str
    last_updated: datetime
    last_updated_by: str
    last_updated_version: str
    created: datetime
    created_by: str
    created_version: str
    canvas_version: int
    pre_automation_time: int
    sla: int
    groups: list[str]
    status: str
    variables: dict
    watchers: list[str]
    ancestors: list[str]
    parent: Parent
    decorators: list[str]
    metrics: Metrics

    def __repr__(self):
        return f"{self._version.value} ({self.name})"
    
    # def __str__(self):
    #     return f"{self.name} - {self._id}"
