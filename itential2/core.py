from typing import Type

from itential2.src.enums import ItentialVersion
from itential2.src.iap_versions import ItentialV2021, ItentialV2023


class Itential:
    @staticmethod
    def create(username: str, password: str, version: ItentialVersion) -> Type["Itential"]:
        match version:
            case ItentialVersion.V2021_1:
                return ItentialV2021(username=username, password=password)
            case ItentialVersion.V2023_1:
                return ItentialV2023(username=username, password=password)
            case _:
                raise ValueError(f"Unsupported version: {version}")
