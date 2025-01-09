from datetime import datetime
from typing import Any

from pydantic import Field

from src import ItentialVersion
from src.base.models.jsonform import JsonFormModel


class JsonFormModel2021_1(JsonFormModel):
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

    def model_dump_import(self):
        """
        Outputs the version required for Itential to import the asset.
        """
        exclude_fields = {"_id", "id", "itential", "_version"}
        return self.model_dump(mode="json", by_alias=True, exclude=exclude_fields)

    def update_server(self):
        """Using the current instance, update the connected server."""
        ...

    def import_server(self):
        """Import the asset instance to the connected server."""
        ...


# Notes:
"""
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
