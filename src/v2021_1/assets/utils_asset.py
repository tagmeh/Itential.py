from typing import TYPE_CHECKING

from src.base import UtilsAsset
from src.exceptions import ApiError

if TYPE_CHECKING:
    from src.v2021_1.itential2021_1 import Itential2021_1


class UtilsAsset2021_1(UtilsAsset):
    def __init__(self, parent: "Itential2021_1"):
        self.parent = parent

    def version(self) -> str:
        """
        Returns a Year.Major.Minor version string of the Itential server.
            e.g. "2021.1.21"
        """
        response = self.parent.call(method="GET", endpoint="/version")
        if response.ok:
            return response.json()
        else:
            raise ApiError(response.status_code, f"Failed to get version: {response.text}", response.json())
