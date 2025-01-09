from datetime import datetime

from pydantic import BaseModel, Field

from src import ItentialVersion
from src.base.models.template import TemplateModel


class TemplateUser(BaseModel):
    class Config:
        populate_by_name = True

    id: str | None = Field(alias="_id", default=None)
    provenance: str | None = None
    username: str | None = None
    first_name: str | None = Field(alias="firstName", default=None)
    inactive: bool | None = None


class TemplateModel2021_1(TemplateModel):
    """Describes a Template (both Jinja2 and TextFSM) in the 2021.1 version of the Itential API"""

    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}

    _version: ItentialVersion = ItentialVersion.V2021_1
    id: str | None = Field(alias="_id", default=None)
    command: str | None = None
    template: str | None = None
    data: str | None = None
    type: str | None = None
    name: str | None = None
    description: str | None = None
    group: str | None = None
    last_updated: datetime | None = Field(alias="lastUpdated", default=None)
    created_by: TemplateUser | str | None = Field(alias="createdBy", default=None)
    last_updated_by: TemplateUser | str | None = Field(alias="lastUpdatedBy", default=None)


# Notes:
"""
Search Templates is the same as Search Transformation.
GET automation-studio/templates
{
	"queryParameters": {
		"equals": {
			"name": "Test TextFSM"
		}
	}
}

Name	Description
limit
integer
(query)
Number of results to return. Used for pagination.

limit - Number of results to return. Used for pagination.
skip
integer
(query)
Number of results to skip. Used for pagination.

skip - Number of results to skip. Used for pagination.
order
integer
(query)
Sort direction, 1 for ascending and -1 for descending.

order - Sort direction, 1 for ascending and -1 for descending.
sort
string
(query)
Field to sort by

sort - Field to sort by
include
string
(query)
Inclusive projection operator formatted as a comma-delineated list. '_id' will be included implicitly unless excluded with 'exclude=_id'. May only be used in conjunction with 'exclude' when 'exclude=_id'.

include - Inclusive projection operator formatted as a comma-delineated list. '_id' will be included implicitly unless excluded with 'exclude=_id'. May only be used in conjunction with 'exclude' when 'exclude=_id'.
exclude
string
(query)
Exclusive projection operator formatted as a comma-delineated list. May only be used in conjunction with 'include' when 'exclude=_id'.

exclude - Exclusive projection operator formatted as a comma-delineated list. May only be used in conjunction with 'include' when 'exclude=_id'.
in
string
(query)
Search for fields exactly matching one of the given list options

in - Search for fields exactly matching one of the given list options
not-in
string
(query)
Search for fields not exactly matching one of the given list options

not-in - Search for fields not exactly matching one of the given list options
equals
string
(query)
Returns results where the specified fields exactly match the given match string(s).

equals - Returns results where the specified fields exactly match the given match string(s).
contains
string
(query)
Returns results where the specified fields contain the given match string(s).

contains - Returns results where the specified fields contain the given match string(s).
starts-with
string
(query)
Returns results where the specified fields start with the given match string(s).

starts-with - Returns results where the specified fields start with the given match string(s).
ends-with
string
(query)
Returns results where the specified fields end in the given match string(s).


GET automation-studio/templates/:id

Get Template by ID
id *
string
(path)
ObjectId specifying a template entity.

id - ObjectId specifying a template entity.
include
string
(query)
Inclusive projection operator formatted as a comma-delineated list. '_id' will be included implicitly unless excluded with 'exclude=_id'. May only be used in conjunction with 'exclude' when 'exclude=_id'.

include - Inclusive projection operator formatted as a comma-delineated list. '_id' will be included implicitly unless excluded with 'exclude=_id'. May only be used in conjunction with 'exclude' when 'exclude=_id'.
exclude
string
(query)
Exclusive projection operator formatted as a comma-delineated list. May only be used in conjunction with 'include' when 'exclude=_id'.



POST automation-studio/templates/import
Expects an array of template json objects.
{
	"templates": []
}


Template has the option to replace instead of import. Import probably creates duplicates.
PUT /automation-studio/templates/:id

Replaces a template document.

Parameters
Try it out
Name	Description
id *
string
(path)
Template id.

id - Template id.
update {}
(body)
Complete template definition to replace the existing template document with. May not contain fields '_id', 'created', 'createdBy', 'lastUpdated', or 'lastUpdatedBy'.

"""
