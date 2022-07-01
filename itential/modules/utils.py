import logging
from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from itential.core import Itential

log = logging.getLogger(__name__)


def index_status(client: "Itential", index: str) -> requests.Response:
    """
    Verify that a collection is properly indexed.
    https://docs.itential.com/2021.1/admin/Itential%20Automation%20Platform/Configuration/#indexing-apis-and-seeding
    All indexes can be found just above at this link:
    https://docs.itential.com/2021.1/admin/Itential%20Automation%20Platform/Configuration/#database-indexes
    """
    return client.call(method="GET", url=f"{client.url}/indexes/{index}/status")


def index_repair(client: "Itential", index: str) -> requests.Response:
    """
    Creates/Repairs all indexes on the server.
    More information can be found here:
    https://docs.itential.com/2021.1/admin/Itential%20Automation%20Platform/Configuration/#database-indexes
    """
    return client.call(method="GET", url=f"{client.url}/indexes/{index}")
