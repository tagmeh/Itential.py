# Base Platform class (Itential) with version handling and authentication
import logging
from typing import Any

import requests

from src.base.assets.job import JobAsset
from src.base.assets.utils import UtilsAsset
from src.base.assets.workflow import WorkflowAsset
from src.exceptions import ApiError

log = logging.getLogger(__name__)


class Itential:
    workflow = WorkflowAsset
    job = JobAsset
    utils = UtilsAsset
    # scripts = Scripts

    def __init__(
        self,
        username: str = "admin@pronghorn",
        password: str = "admin",
        server_url: str = "http://localhost:3000",
        **kwargs: Any,
    ) -> None:
        log.debug("Initializing Auth class instance.")
        self.username: str = username
        self.password: str = password

        self._url: str = server_url

        self.session: requests.Session = kwargs.get("session", requests.Session())
        self.auth_body: dict[str, dict[str, str]] = {"user": {"username": self.username, "password": self.password}}
        self.authenticate()

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str) -> None:
        """Cleans the input URL of any extra whitespace and trailing slashes."""
        value = value.strip()
        while value.endswith("/"):
            value = value[::-1].replace("/", "", 1)[::-1]
        self._url = value

    @staticmethod
    def get_login_path() -> str:
        """
        Returns the login path for the Itential server.
        Override this method within the version-specific Itential class (ie Itential2021_1)
          if the login path is different.
        """
        return "/login/"

    def authenticate(self) -> None:
        login_path = self.get_login_path()
        log.debug(f"Authenticating with {self.url} server using {login_path} endpoint.")
        response = self.session.post(f"{self.url}{login_path}", json=self.auth_body, verify=False)
        if response.ok:
            log.debug(f"Authenticated with {self.url} server. [{response.status_code}]")
        else:
            log.error(
                f"{response.status_code} - Failed to authenticate with {self.url} server. "
                f"Reason: '{response.json()['message']}'"
            )
            raise ApiError(
                response.status_code, f"Failed to authenticate with {self.url} server.", response_data=response.json()
            )

    def call(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
        url = f"{self.url}/{endpoint}"
        headers = kwargs.get("headers", {"Content-Type": "application/json"})
        verify = kwargs.get("verify", False)
        try:
            # Todo: Setup re-auth attempts up to like, n times, then throw APIError
            response = self.session.request(method=method, url=url, headers=headers, verify=verify, **kwargs)
            if response.status_code == 401:  # Unauthorized, re-authenticate and retry
                self.authenticate()
                response = self.session.request(method=method, url=url, headers=headers, verify=verify, **kwargs)
            return response
        except requests.RequestException as e:
            log.error(f"API connection error: {e}")
            raise ApiError(500, "Connection error", str(e)) from e
