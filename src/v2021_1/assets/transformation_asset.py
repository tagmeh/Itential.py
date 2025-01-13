import logging
from typing import Any, Union, TYPE_CHECKING

from src.base import JsonFormAsset
from src.exceptions import ApiError
from src.v2021_1.models.transformation_model import TransformationModel2021_1

if TYPE_CHECKING:
    from src.v2021_1.itential2021_1 import Itential2021_1


log = logging.getLogger(__name__)


class JsonFormAsset2021_1(JsonFormAsset):
    def __init__(self, parent: "Itential2021_1"):
        self.parent = parent

    def retrieve(self, jst_id: str) -> TransformationModel2021_1:
        """Retrieves a Transformation by its ID."""

        response = self.parent.call(method="GET", endpoint=f"/transformations/{jst_id}")
        if response.ok:
            return TransformationModel2021_1(itential_instance=self.parent, **response.json())
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    def search(self) -> list[TransformationModel2021_1]:
        """Retrieves a list of all Transformations."""

        response = self.parent.call(method="GET", endpoint="/transformations")
        if response.ok:
            transformations = response.json()
            return [
                TransformationModel2021_1(itential_instance=self.parent, **transformation)
                for transformation in transformations
            ]

    def update(self, jst_id: str, payload: dict[str, Any]) -> TransformationModel2021_1:
        """Updates a Transformation by its ID."""
        response = self.parent.call(method="PUT", endpoint=f"/transformations/{jst_id}", json=payload)
        if response.ok:
            return TransformationModel2021_1(itential_instance=self.parent, **response.json())
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    def upload(self, payload: dict[str, Any]) -> TransformationModel2021_1:
        """Uploads a new Transformation."""
        response = self.parent.call(method="POST", endpoint="/transformations", json=payload)
        if response.ok:
            return TransformationModel2021_1(itential_instance=self.parent, **response.json())
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    def delete(self, jst_id: str) -> None:
        """Deletes a Transformation by its ID."""
        response = self.parent.call(method="DELETE", endpoint=f"/transformations/{jst_id}")
        if not response.ok:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )
