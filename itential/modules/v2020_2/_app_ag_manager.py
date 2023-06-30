"""
Link to Itential Docs: https://apidocs.itential.com/2020.2/api/app-ag_manager/

Implemented  Doc String  Tests
    [x]         [x]       [ ]   discoverModules
    [x]         [x]       [ ]   undiscoverAll
    [x]         [x]       [ ]   undiscoverModules
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from itential.core import Itential
    import requests


class AppAgManager:
    """https://apidocs.itential.com/2020.2/api/app-ag_manager/"""

    def __init__(self, client: "Itential"):
        self.client = client

    def discover_modules(self, adapter_id: str) -> "requests.Response":
        """
        Discovers all actions from a specified IAG adapter.
        This will restart this app and display a corresponding log message.
        https://apidocs.itential.com/2020.2/api/app-ag_manager/discoverModules/

        :param adapter_id: Automation Gateway adapter ID
        :return: requests.Response: A pronghorn.json object.
        """
        return self.client.call(method="GET", url=f"{self.client.url}/ag-manager/actions/{adapter_id}")

    def undiscover_all(self) -> "requests.Response":
        """
        Discovers all actions from all IAG adapters.
        This will restart this app and display a corresponding log message.
        https://apidocs.itential.com/2020.2/api/app-ag_manager/undiscoverAll/

        :return: requests.Response: A pronghorn.json object.
        """
        return self.client.call(method="DELETE", url=f"{self.client.url}/ag-manager/actions")

    def undiscover_modules(self, adapter_id: str) -> "requests.Response":
        """
        Removes all actions from a specified IAG adapter.
        This will restart this app and display a corresponding log message.
        https://apidocs.itential.com/2020.2/api/app-ag_manager/undiscoverModules/

        :param adapter_id: Automation Gateway adapter ID
        :return: requests.Response: A pronghorn.json object.
        """
        return self.client.call(method="DELETE", url=f"{self.client.url}/ag-manager/actions/{adapter_id}")
