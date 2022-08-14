"""
Link to Itential Docs: https://apidocs.itential.com/2020.2/api/app-admin_essentials/

Implemented  Doc String  Tests
    [x]         [/]       [ ]   getServicesHealth
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from itential.core import Itential
    import requests


class AppAdminEssentials:
    """https://apidocs.itential.com/2020.2/api/app-admin_essentials/"""

    @staticmethod
    def get_services_health(client: "Itential") -> "requests.Response":
        """
        Gets the health of all services in an IAP environment.
        https://apidocs.itential.com/2020.2/api/app-admin_essentials/getServicesHealth/
        :param client: Itential state object
        :return:
        """
        return client.call(method="GET", url=f"{client.url}/admin/services/health")
