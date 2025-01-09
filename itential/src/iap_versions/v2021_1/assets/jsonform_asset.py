import logging

from itential.src.exceptions import ApiError
from itential.src.iap_versions.v2021_1.models.jsonform2021_1 import JsonForm2021_1

# if TYPE_CHECKING:
#     from itential.src.iap_versions.v2021_1.itential2021_1 import Itential2021_1

log = logging.getLogger(__name__)


class JsonFormAsset:
    # def __init__(self, parent: "Itential2021_1"):
    def __init__(self, parent):
        self.parent = parent

    def retrieve(self, jsonform_id: str) -> JsonForm2021_1:
        response = self.parent.call(method="GET", endpoint=f"/json-forms/forms/{jsonform_id}")
        if response.ok:
            return JsonForm2021_1(itential_instance=self.parent, **response.json())
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    def update(self, jsonform: dict | JsonForm2021_1) -> JsonForm2021_1:
        """
        The JSON form asset has the ability to update in-place (unlike the workflow asset).
        Requires the '_id' param and the JSON form parameters to update.
        Capable of a partial update.
        """

        payload = {"options": None}

        if isinstance(jsonform, dict):
            jsonform_id = jsonform["_id"]
            payload["options"] = jsonform
        elif isinstance(jsonform, JsonForm2021_1):
            jsonform_id = jsonform.id
            payload["options"] = jsonform.model_dump_import()
        else:
            raise ValueError("'jsonform' must be a json-form dict or JsonForm2021_1 instance.")

        response = self.parent.call(method="PUT", endpoint=f"/json-forms/forms/{jsonform_id}", json=payload)
        print(f"{response.json()=}")
        # if response.ok:
        #     return JsonForm2021_1(itential_instance=self.parent, **response.json())
        # else:
        #     raise ApiError(
        #         response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
        #     )

    def upload(self, jsonforms: list[dict] | list[JsonForm2021_1]) -> list[str]:
        """
        Capable of importing more than one json form at the same time.
        """

        payload = {"forms": []}

        if len(jsonforms) == 0:
            raise ValueError("Must pass in at least one json form object.")

        if isinstance(jsonforms[1], dict):
            payload["forms"] = jsonforms
        elif isinstance(jsonforms[1], JsonForm2021_1):
            payload["forms"] = [jsonform.model_dump_import() for jsonform in jsonforms]
        else:
            raise ValueError("Indexes must be of type dict or JsonForm2021_1")

        response = self.parent.call(method="POST", endpoint="/json-forms/forms/import", json=payload)
        print(f"{response.json()=}")
        # if response.ok:
        #     return JsonForm2021_1(itential_instance=self.parent, **response.json())
        # else:
        #     raise ApiError(
        #         response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
        #     )
        # Return a list of the imported strings, or the objects. Depending on response.
