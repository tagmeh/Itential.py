import logging
from enum import Enum
from typing import Dict, Any

import requests

logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)


class SupportedVersion(Enum):
    V2020_2 = "2020.2"
    V2021_1 = "2021.1"
    V2021_2 = "2021.2"
    V2023_1 = "2023.1"


class Core:
    """
    Accepts a username and password to authenticate with the Itential server.
    Contains the default auth values for the local server.
    Stores the requests session object.
    Responsible for re-authentication if the session is invalid.
    """
    def __init__(self, username: str, password: str, url: str, **kwargs) -> None:
        self.username: str = username
        self.password: str = password

        self._url: str = url
        # self._url - Probably a better way to do this.
        # self.__setattr__('url', kwargs.get('url', "http://localhost:3000"))

        self.session: requests.Session = kwargs.get('session', requests.Session())
        self.auth_body: dict[str, dict[str, str]] = {"user": {"username": self.username, "password": self.password}}
        self.authenticate()

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str) -> None:
        """Cleans the input URL of any extra whitespace and trailing slashes."""
        if value:
            trimmed_value = value.strip()
            if trimmed_value.endswith('/'):
                value = trimmed_value[::-1].replace('/', '', 1)[::-1]
            self._url = value

    def authenticate(self) -> None:
        response = self.session.post(f"{self.url}/login/", json=self.auth_body, verify=False)
        if response.ok:
            log.debug(f"Authenticated with {self.url} server. [{response.status_code}]")
        else:
            log.error(f"{response.status_code} - Failed to authenticate with {self.url} server. "
                      f"Reason: '{response.json()['message']}'")

    def call(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
        url = f"{self.url}/{endpoint}"
        headers = kwargs.get("headers", {"Content-Type": "application/json"})
        verify = kwargs.get("verify", False)
        response = self.session.request(method=method, url=url, headers=headers, verify=verify, **kwargs)
        if response.status_code == 401:  # Unauthorized, re-authenticate and retry
            self.authenticate()
            response = self.session.request(method=method, url=url, headers=headers, verify=verify, **kwargs)
        return response


class Itential(Core):
    def __init__(self, username: str, password: str, url: str = "http://localhost:3000", **kwargs) -> None:  # type: ignore
        # Todo: self.version may need to move to Core if there become more than one endpoint to authenticate with.
        self.version = kwargs.get('version')
        super().__init__(username=username, password=password, url=url, **kwargs)


    def call(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        """
        Wrapper for the Requests request method. Designed to have the Itential class authenticate with the server
        or verify its connection before making the module call.
        """
        self.authenticate()

        headers = kwargs.get("headers", {"Content-Type": "application/json"})  # Required by some calls.
        verify = kwargs.get("verify", False)

        return self.session.request(method=method, url=url, headers=headers, verify=verify, **kwargs)

    def authenticate(self) -> None:
        """
        Authenticates with the specified server. Attempts to use self.session if available.
        Updates the self.session for use with subsequent calls.
        """
        # Make initial authentication check with old/previous session cookies.
        if not self.get_version_health_check().ok:
            log.debug('Initial Health Check failed. Authenticating with server.')
            self.verify_remote_auth_info()  # Verifies username and prompts for the password.
            self._authenticate_call()  # Authenticate with server

    def _authenticate_call(self) -> None:
        response = self.session.post(f"{self.url}/login/", json=self.auth_body, verify=False)
        if response.ok:
            self.password = "admin"  # Reset to default password for local access.
            log.debug(f"Authenticated with {self.url} server. [{response.status_code}]")
        else:
            log.error(
                f"{response.status_code} - Failed to authenticate with {self.url} server. "
                f"Reason: '{response.json()['message']}'"
            )

    def get_version_health_check(self) -> requests.Response:
        """
        Pulls a dictionary of all currently installed apps/adapters on the server, it's status, and versions.
        Also labeled as a health check in the IAP docs.
        Used as a quick test to verify the current session object before attempting to (re)authenticate.
        """
        response: requests.Response = self.session.get(url=f"{self.url}/health/applications")
        log.debug(f"Health check: {response.status_code}")
        return response

    def verify_remote_auth_info(self) -> None:
        """
        Holdover method from when this was a TUI app.
        Need to validate there's a valid username/password or not. If not, we'd use the default
        information for authentication, unless given something different.
        """
        if not self.username:
            raise ValueError("Must have a Username to authenticate with server.")
        log.debug(f"Username validated: '{self.username}'")

        if not self.password:
            assert isinstance(self.password, str), "A password is required."
        log.debug("Password validated.")
