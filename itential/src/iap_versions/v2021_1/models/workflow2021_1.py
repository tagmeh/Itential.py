from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from itential.src.iap_versions.base import Workflow
from itential.src.versions import ItentialVersion


class WorkflowUser(BaseModel):

    class Config:
        populate_by_name = True

    provenance: str | None = None
    username: str | None = None
    first_name: str | None = Field(alias="firstname", default=None)
    inactive: bool | None = None


class WorkflowError(BaseModel):

    class Config:
        populate_by_name = True

    task: str | None = None
    name: str | None = None
    message: str | None = None


class Workflow2021_1(Workflow):
    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}

    _version: ItentialVersion = ItentialVersion.V2021_1
    id: str | None = Field(alias="_id", default=None)
    name: str | None = None
    type: str | None = None
    tasks: dict[str, dict[str, Any]] | None = None
    transitions: dict[str, dict[str, Any]] | None = None
    font_size: int | None = None
    last_updated: datetime | None = None
    last_updated_by: WorkflowUser | str | None = None  # str is if user is not expanded.
    last_updated_version: str | None = Field(alias="lastUpdatedVersion", default=None)
    input_schema: dict | None = Field(alias="inputSchema", default={})
    output_schema: dict | None = Field(alias="outputSchema", default={})
    created: datetime | None = None
    created_by: WorkflowUser | str | None = None  # str is if user is not expanded.
    created_version: str | None = Field(alias="createdVersion", default=None)
    canvas_version: int | None = Field(alias="canvasVersion", default=None)
    tags: list[str] | None = None
    groups: list[str] | None = None
    errors: list[WorkflowError] | None = None

    def model_dump_to_import(self):
        """
        Outputs the version required for Itential to import the workflow.
        aka, no '_id' and 'errors' property.
        """
        exclude_fields = {"_id", "id", "_itential", "version", "errors"}
        return self.model_dump(mode="json", by_alias=True, exclude=exclude_fields)
