import logging
from typing import Dict, Any

import requests
from requests.adapters import HTTPAdapter, Retry

log = logging.getLogger(__name__)


class Itential:
    def __init__(self, **kwargs) -> None:  # type: ignore
        """
        :param username: Known defaults include "admin@pronghorn" and "admin@itential"
        :param password: For authenticating with the server. Never stored or printed.
        :param url: Used to change the server. Default is the local machine.
        :param session: Pass in a previously saved requests.Session object in order to bypass the authentication call.
        :param max_retries: The maximum number of times to retry a failed request. Default is 3.
        :param backoff_factor: The factor to multiply the backoff time by. Default is 0.2.
                               0.2 is a 20% increase per backoff.
        :param backoff_delay: The initial delay to use. Default is 2.
        """
        self.username: str = kwargs.get("username", "admin@pronghorn")
        self.password: str = kwargs.get("password", "admin")
        self.auth_body: Dict[str, Dict[str, str]] = {"user": {"username": self.username, "password": self.password}}
        self.url: str = self.clean_and_validate_url(kwargs.get("url", "http://localhost:3000"))
        self.session: requests.Session = kwargs.get('session', requests.Session())

        self.max_retries: int = kwargs.get("max_retries", 3)

        self.backoff_factor: float = float((kwargs.get("backoff_factor", 0.2)))
        if self.backoff_factor < 0:
            log.warning("backoff_factor cannot be less than 0. Setting to 0.1 (10%).")
            self.backoff_factor = 0.1

        self.backoff_delay: int = kwargs.get("backoff_delay", 2)
        if self.backoff_delay < 1:
            log.warning("backoff_delay is less than 1. Setting to 1.")
            self.backoff_delay = 1

        self.setup_requests_retry()

    def setup_requests_retry(self):
        """
        Sets up the retry mechanism for the requests library.
        """
        status_forcelist = [
            408,  # Request Timeout
            409,  # Conflict
            429,  # Too Many Requests
            500,  # Internal Server Error
            502,  # Bad Gateway
            503,  # Service Unavailable
            504,  # Gateway Timeout
        ]
        log.debug(
            f'Configuring Requests retry for status codes: {", ".join([str(status) for status in status_forcelist])}'
        )

        retry = Retry(
            total=self.max_retries,
            backoff_factor=self.backoff_factor,
            status_forcelist=status_forcelist
        )
        log.debug(f'Configured requests.Retry for with '
                  f'max_retries={self.max_retries} and backoff_factor={self.backoff_factor}')

        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        log.debug('Retry set for "http://"')
        self.session.mount('https://', adapter)
        log.debug('Retry set for "https://"')

    @staticmethod
    def clean_and_validate_url(value: str) -> str:
        """Cleans the input URL of any extra whitespace and trailing slashes."""
        log.debug(f'Cleaning/validating user-defined URL: {value}')
        if value:
            trimmed_value = value.strip()
            if trimmed_value.endswith('/'):
                value = trimmed_value[::-1].replace('/', '', 1)[::-1]
            log.debug(f'Cleaned/validated URL: {value}')
            return value

    def call(self, method: str, url: str, **kwargs: Any) -> requests.Response:
        """
        Calls the given endpoint, authenticates with the server if necessary.
        """
        headers = kwargs.get("headers", {"Content-Type": "application/json"})  # Required by some calls.
        verify = kwargs.get("verify", False)
        # retry is only here to prevent a loop. Causes errors if passed into session.request, thus, we pop it.
        retry = kwargs.pop('retry', False)

        response = self.session.request(method=method, url=url, headers=headers, verify=verify, **kwargs)

        if response.status_code in [401, 403] and not retry:
            self.authenticate()
            return self.call(method=method, url=url, retry=True, **kwargs)  # Retry the call after authenticating.
        return response

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
        response: requests.Response = self.session.get(url=f"{self.url}/health/applications", verify=False)
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
