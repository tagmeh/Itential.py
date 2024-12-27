from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from itential.src.iap_versions.base.models import Job, Workflow
from itential.src.versions import ItentialVersion


class JobMetrics(BaseModel):
    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.fromtimestamp()}

    start_time: datetime | None = None
    user: str | None = None
    progress: int | float | None = None
    end_time: datetime | None = None  # A Job that is not yet completed will not have an "end_time" field.


class JobError(BaseModel):
    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.fromtimestamp()}

    message: str | None = None
    task: str | None = None
    timestamp: datetime | None = None


class Job2023_1(Job):
    """Describes a job in the 2023.1 version of the Itential API"""

    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.fromisoformat()}

    version: ItentialVersion = ItentialVersion.V2023_1
    id: str | None = Field(alias="_id", default=None)
    name: str | None = None
    tasks: dict[str, dict[str, Any]] | None = None
    transitions: dict[str, dict[str, Any]] | None = None
    canvas_version: int | None = Field(alias="canvasVersion", default=None)
    type: str | None = None
    font_size: int | None = None
    # error_handler: str | None = Field(alias="errorHandler", default=None)
    # Getting error: Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
    pre_automation_time: int | None = Field(alias="preAutomationTime", default=None)
    sla: int | None = None
    groups: list[str] | None = None
    last_updated: datetime | None = None
    last_updated_version: str | None = Field(alias="lastUpdatedVersion", default=None)
    created: datetime | None = None
    created_by: str | None = None
    created_version: str | None = Field(alias="createdVersion", default=None)
    encoding_version: int | None = Field(alias="encodingVersion", default=None)
    last_updated_by: str | None = None
    description: str | None = None
    status: str | None = None
    variables: dict | None = None
    watchers: list[str] | None = None
    ancestors: list[str] | None = None
    decorators: list[str] | None = None
    metrics: JobMetrics | None = None
    error: list[JobError] | None = None


class WorkflowUser(BaseModel):
    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.fromisoformat()}

    id: str | None = Field(alias="_id", default=None)
    provenance: str | None = None
    username: str | None = None
    first_name: str | None = Field(alias="firstname", default=None)
    inactive: bool | None = None
    last_login: datetime | None = Field(alias="lastLogin", default=None)


class WorkflowError(BaseModel):
    class Config:
        populate_by_name = True

    task: str | None = None
    name: str | None = None
    message: str | None = None


class BaseWorkflow2023_1(Workflow):
    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.fromisoformat()}

    version: ItentialVersion = ItentialVersion.V2023_1
    name: str | None = None
    type: str | None = None
    tasks: dict[str, dict[str, Any]] | None = None
    transitions: dict[str, dict[str, Any]] | None = None
    font_size: int | None = None
    last_updated: datetime | None = None
    last_updated_by: WorkflowUser | None = None
    last_updated_version: str | None = Field(alias="lastUpdatedVersion", default=None)
    input_schema: dict | None = Field(alias="inputSchema", default={})
    output_schema: dict | None = Field(alias="outputSchema", default={})
    created: datetime | None = None
    created_by: WorkflowUser | None = None
    created_version: str | None = Field(alias="createdVersion", default=None)
    canvas_version: int | None = Field(alias="canvasVersion", default=None)
    tags: list[str] | None = None
    groups: list[str] | None = None


class ExportedWorkflow2023_1(BaseWorkflow2023_1):
    """A platform (but not version) agnostic representation of a workflow."""

    pass


class Workflow2023_1(BaseWorkflow2023_1):
    """A Representation of a workflow as it exists within the platform."""

    class Config:
        populate_by_name = True

    id: str | None = Field(alias="_id", default=None)
    errors: list[WorkflowError] | None = None
