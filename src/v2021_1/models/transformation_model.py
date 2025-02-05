from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from src.base.models.transformation import TransformationModel
from src.versions import ItentialVersion


class TransformationUser(BaseModel):
    class Config:
        populate_by_name = True

    id: str | None = Field(alias="_id", default=None)
    provenance: str | None = None
    username: str | None = None


class TransformationModel2021_1(TransformationModel):
    """Describes a Transformation/JST in the 2021.1 version of the Itential API"""

    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}

    _version: ItentialVersion = ItentialVersion.V2021_1
    id: str | None = Field(alias="_id", default=None)
    name: str | None = None
    description: str | None = None
    incoming: dict[str, Any] | None = None
    outgoing: dict[str, Any] | None = None
    steps: list[dict[str, Any]] | None = None
    functions: list[dict[str, Any]] | None = None
    comments: list[dict[str, Any]] | None = None
    view: dict[str, int] | None = None
    created: datetime | None = None
    created_by: TransformationUser | str | None = Field(alias="createdBy", default=None)
    last_updated: datetime | None = Field(alias="lastUpdated", default=None)
    last_updated_by: TransformationUser | str | None = Field(alias="lastUpdatedBy", default=None)
    version: str | None = None
    tags: list[str] | None = None


# Notes:
"""
Get transformation by ID
GET transformations/:id 
Only url params.

Search Transformations
GET /transformations
Can use params object: Seems similar to the 2023_1 getJobs GET endpoint.
{
    "queryParameters": {
        "contains": {
            "name": "test_transformation"
        }
    }
}

{
    "queryParameters": {
        "equals": {
            "name": "test_transformation"
        }
    }
}
"""
