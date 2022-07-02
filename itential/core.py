import logging
from typing import Dict, Any

import requests

logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)


class Itential:
    def __init__(self, **kwargs) -> None:  # type: ignore
        """
        :param username: Know defaults include "admin@pronghorn" and "admin@itential"
        :param password: For authenticating with the server. Never stored or printed.
        :param version: Not in use yet, might help with using the correct methods for authentication in the future.
        :param url: Used to change the server. Default is the local machine.
        :param session: Pass in a previously saved requests.Session object in order to bypass the authentication call.
        """
        self.username: str = kwargs.get("username", "admin@pronghorn")
        self.password: str = kwargs.get("password", "admin")
        self.version: str = kwargs.get("version", "latest")
        self.url: str = kwargs.get("url", "http://localhost:3000")
        self.auth_body: Dict[str, Dict[str, str]] = {"user": {"username": self.username, "password": self.password}}

        self.session: requests.Session = kwargs.get('session', requests.Session())

    def call(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        """
        Wrapper for the Requests request method. Designed to have the Itential class authenticate with the server
        or verify it's connection before making the module call.
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


if __name__ == '__main__':
    client = Itential()
    client.authenticate()
    print(client.session)
