"""
Link to Itential Docs: https://docs.itential.com/2020.2/api/app-ag_manager/

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
    """https://docs.itential.com/2020.2/api/app-ag_manager/"""

    @staticmethod
    def discover_modules(client: "Itential", adapter_id: str) -> "requests.Response":
        """
        Discovers all actions from a specified IAG adapter.
        This will restart this app and display a corresponding log message.
        https://docs.itential.com/2020.2/api/app-ag_manager/discoverModules/
        :param client: Itential state object
        :param adapter_id: Automation Gateway adapter ID
        :return: requests.Response: A pronghorn.json object.
        """
        return client.call(method="GET", url=f"{client.url}/ag-manager/actions/{adapter_id}")

    @staticmethod
    def undiscover_all(client: "Itential") -> "requests.Response":
        """
        Discovers all actions from all IAG adapters.
        This will restart this app and display a corresponding log message.
        https://docs.itential.com/2020.2/api/app-ag_manager/undiscoverAll/
        :param client: Itential state object
        :return: requests.Response: A pronghorn.json object.
        """
        return client.call(method="DELETE", url=f"{client.url}/ag-manager/actions")

    @staticmethod
    def undiscover_modules(client: "Itential", adapter_id: str) -> "requests.Response":
        """
        Removes all actions from a specified IAG adapter.
        This will restart this app and display a corresponding log message.
        https://docs.itential.com/2020.2/api/app-ag_manager/undiscoverModules/
        :param client: Itential state object
        :param adapter_id: Automation Gateway adapter ID
        :return: requests.Response: A pronghorn.json object.
        """
        return client.call(method="DELETE", url=f"{client.url}/ag-manager/actions/{adapter_id}")
