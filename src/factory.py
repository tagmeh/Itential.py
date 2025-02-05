# Factory function for creating platform instances based on version
from src.base.itential import Itential
from src.v2021_1.itential2021_1 import Itential2021_1
from src.versions import ItentialVersion


def create_itential(
    version: ItentialVersion,
    username: str = "admin@pronghorn",
    password: str = "admin",
    server_url: str = "http://localhost:3000",
) -> Itential:
    """
    Factory function for creating platform instances based on version
    """
    version_map = {
        ItentialVersion.V2021_1: Itential2021_1,
        # ItentialVersion.V2023_1: Itential2023_1,
    }

    return version_map[version](username=username, password=password, server_url=server_url)
