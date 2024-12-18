from datetime import datetime

from pydantic import BaseModel, Field

from itential2.src.versions import SupportedVersion
from itential2.src.asset_classes.asset_versions.base import Job, Workflow


class JobMetrics(BaseModel):
    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.fromtimestamp()
        }

    start_time: datetime
    user: str
    progress: int | float
    end_time: datetime = None  # A Job that is not yet completed will not have an "end_time" field.


class JobError(BaseModel):
    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.fromtimestamp()
        }

    message: str = None
    task: str = None
    timestamp: datetime = None


class Job2023_1(Job):
    """ Describes a job in the 2023.1 version of the Itential API """

    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.fromisoformat()
        }

    _version: SupportedVersion = SupportedVersion.V2023_1
    _id: str = None
    name: str = None
    # tasks
    # transitions
    canvas_version: int = Field(alias="canvasVersion", default=None)
    type: str = None
    font_size: int = None
    # error_handler: str = Field(alias="errorHandler", default=None)
    # Getting error: Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
    pre_automation_time: int = Field(alias="preAutomationTime", default=None)
    sla: int = None
    groups: list[str] = None
    last_updated: datetime = None
    last_updated_version: str = Field(alias="lastUpdatedVersion", default=None)
    created: datetime = None
    created_by: str = None
    created_version: str = Field(alias="createdVersion", default=None)
    encoding_version: int = Field(alias="encodingVersion", default=None)
    last_updated_by: str = None
    description: str = None
    status: str = None
    variables: dict = None
    watchers: list[str] = None
    ancestors: list[str] = None
    decorators: list[str] = None
    metrics: JobMetrics = None
    error: list[JobError] = None

    def __repr__(self):
        return f"{self._version.value} ({self.name})"

    def __str__(self):
        return f"Name: {self.name} ID: {self._id}"


class WorkflowUser(BaseModel):
    class Config:
        populate_by_name = True

    provenance: str = None
    username: str = None
    first_name: str = Field(alias="firstname", default=None)
    inactive: bool = None


class WorkflowError(BaseModel):
    class Config:
        populate_by_name = True

    task: str = None
    name: str = None
    message: str = None


class BaseWorkflow2023_1(Workflow):
    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.fromisoformat()
        }

    name: str = None
    type: str = None
    tasks: dict = None
    transitions: dict = None
    font_size: int = None
    last_updated: datetime = None
    last_updated_by: WorkflowUser = None
    last_updated_version: str = Field(alias="lastUpdatedVersion", default=None)
    input_schema: dict = Field(alias="inputSchema", default_factory=dict)
    output_schema: dict = Field(alias="outputSchema", default_factory=dict)
    created: datetime = None
    created_by: WorkflowUser = None
    created_version: str = Field(alias="createdVersion", default=None)
    canvas_version: int = Field(alias="canvasVersion", default=None)
    tags: list[str] = None
    groups: list[str] = None


class ExportedWorkflow2023_1(BaseWorkflow2023_1):
    pass


class Workflow2023_1(BaseWorkflow2023_1):
    _id: str = None
    errors: list[WorkflowError] = None
