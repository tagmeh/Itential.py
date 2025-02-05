import logging
from typing import Any, Union

from src.base import JsonFormAsset
from src.exceptions import ApiError
from src.v2021_1.models.jsonform_model import JsonFormModel2021_1

log = logging.getLogger(__name__)


class JsonFormAsset2021_1(JsonFormAsset):
    # def __init__(self, parent: "Itential2021_1"):
    def __init__(self, parent):
        self.parent = parent

    def retrieve(self, jsonform_id: str) -> JsonFormModel2021_1:
        """Retrieves a JsonForm by its ID."""

        response = self.parent.call(method="GET", endpoint=f"/json-forms/forms/{jsonform_id}")
        if response.ok:
            return JsonFormModel2021_1(itential_instance=self.parent, **response.json())
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    def search(self, contains: dict[str, Any] = None, equals: dict[str, Any] = None) -> list[JsonFormModel2021_1]:
        """
        Queries the Itential API for all JSON forms.
        The documentation for this API is missing, so most of the query parameters are unknown.

        payload: {
            "queryParameters": {
                "equals": {
                    "name": "Cool JsonForm"
                },
                "contains": {
                    "name": "Cool"
                }
            }
        }
        """

        params = {"queryParameters": {}}

        if contains:
            params["contains"] = contains

        if equals:
            params["equals"] = equals

        if contains and equals:
            log.warning("JsonFormAsset Search(): 'contains' and 'equals' parameters can clash. Use with caution.")

        response = self.parent.call(method="GET", endpoint="/json-forms/forms", params=params)

        if response.ok:
            json_forms = response.json()
            return [JsonFormModel2021_1(itential_instance=self.parent, **json_form) for json_form in json_forms]
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    def update(self, jsonform: dict | JsonFormModel2021_1) -> str:
        """
        The JSON form asset has the ability to update in-place (unlike the workflow asset).
        Requires the '_id' param and the JSON form parameters to update.
        Capable of a partial update.

        Partial (Important fields) Response Example:
        {
            "status": {
                "result": {
                    "n": 1,
                    "nModified": 1,
                    "ok": 1
                },
                "modifiedCount": 1,
                "matchedCount": 1,
                "ok": 1
            },
            "message": "Form Updated"
        }
        """

        payload = {"options": None}

        if isinstance(jsonform, dict):
            jsonform_id = jsonform["_id"]
            payload["options"] = jsonform

        elif isinstance(jsonform, JsonFormModel2021_1):
            jsonform_id = jsonform.id
            payload["options"] = jsonform.model_dump_import()

        else:
            raise ValueError("'jsonform' must be a json-form dict or JsonForm2021_1 instance.")

        response = self.parent.call(method="PUT", endpoint=f"/json-forms/forms/{jsonform_id}", json=payload)
        if response.ok:
            response_json = response.json()
            return response_json["message"]
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    def upload(self, jsonforms: list[dict] | list[JsonFormModel2021_1]) -> dict[str, str]:
        """
        Capable of importing more than one json form at the same time.
        Importing a jsonform that already exists will generate a new jsonform with an "(n)" suffix.
        We avoid the suffix by deleting the jsonform before uploading it.
        """

        # Todo: Consider revising the upload method. Instead of deleting the jsonform before uploading, perhaps
        #  it's safer to update() the jsonform if it exists, and import if it doesn't.

        if len(jsonforms) == 0:
            raise ValueError("Must pass in at least one json form object.")

        forms = []

        for form in jsonforms:
            if isinstance(form, dict):
                forms.append(form)
            elif isinstance(form, JsonFormModel2021_1):
                forms.append(form.model_dump_import())
            else:
                raise ValueError("Indexes must be of type dict or JsonForm2021_1")

        form_ids = [form["_id"] for form in forms]
        self.delete(ids=form_ids)

        payload = {"forms": forms}

        response = self.parent.call(method="POST", endpoint="/json-forms/forms/import", json=payload)
        if response.ok:
            response_json = response.json()
            log.info(f"Imported {response_json['message']}")
            return {"status": response_json["status"], "message": response_json["message"]}

        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    def delete(self, ids: list[str]) -> dict[str, Union[str, int]]:
        """
        Deletes a JSON form by its ID.
        """

        payload = {"ids": ids}

        response = self.parent.call(method="DELETE", endpoint="/json-forms/forms", json=payload)
        if response.ok:
            response_json = response.json()
            log.info(f"Deleted {response_json['deleted']} JsonForms.")
            return {"status": response_json["status"], "deleted": response_json["deleted"]}
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )
