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

    def __init__(self, client: "Itential"):
        self.client = client

    def get_services_health(self) -> "requests.Response":
        """
        Gets the health of all services in an IAP environment.
        https://apidocs.itential.com/2020.2/api/app-admin_essentials/getServicesHealth/

        :return:
        """
        return self.client.call(method="GET", url=f"{self.client.url}/admin/services/health")
