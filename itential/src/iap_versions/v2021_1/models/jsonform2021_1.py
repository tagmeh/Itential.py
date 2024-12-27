from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from itential.src.iap_versions.base.models import JsonForm
from itential.src.versions import ItentialVersion


class JsonForm2021_1(JsonForm):
    """Describes a JsonForm in the 2021.1 version of the Itential API"""

    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}

    _version: ItentialVersion = ItentialVersion.V2021_1
    id: str | None = Field(alias="_id", default=None)
    created: datetime | None = None
    created_by: str | None = Field(alias="createdBy", default=None)
    last_updated: datetime | None = Field(alias="lastUpdated", default=None)
    last_updated_by: str | None = Field(alias="lastUpdatedBy", default=None)
    name: str | None = None
    description: str | None = None
    struct: dict[str, Any] | None = None
    schema: dict[str, Any] | None = None
    ui_schema: dict[str, Any] | None = Field(alias="uiSchema", default=None)
    binding_schema: dict[str, Any] | None = Field(alias="bindingSchema", default=None)
    validation_schema: dict[str, Any] | None = Field(alias="validationSchema", default=None)
    version: str | None = None


# Notes:
"""
GET by ID
GET /json-forms/forms/:id

id *
string
(path)
Unique name of the form

Update by ID
PUT /json-forms/forms/:id

id *
string
(path)
The ID of the form.

id - The ID of the form.
options *
(body)
object containing the fields to be updated


Import By Json
POST /json-forms/forms/import

forms *
(body)
Array of forms


"""
