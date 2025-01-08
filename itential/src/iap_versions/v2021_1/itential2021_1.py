import logging
from typing import Any

from itential.src.auth import Auth
from itential.src.iap_versions.v2021_1.assets.job_asset import JobAsset
from itential.src.iap_versions.v2021_1.assets.jsonform_asset import JsonFormAsset
from itential.src.iap_versions.v2021_1.assets.scripts import Scripts
from itential.src.iap_versions.v2021_1.assets.workflow_asset import WorkflowAsset
from itential.src.versions import ItentialVersion

log = logging.getLogger(__name__)


class Itential2021_1(Auth):
    version = ItentialVersion.V2021_1

    def __init__(self, username: str = None, password: str = None, url: str = None, **kwargs: Any):
        log.debug("Initializing Itential 2021.1 class instance.")
        # Imported like this to allow automatic authentication and session handling via the call() method.
        Auth.__init__(self, username=username, password=password, url=url, **kwargs)
        # Import subclasses
        log.debug("Initializing Itential 2021.1 subclasses.")
        self.scripts = Scripts(self)
        self.job = JobAsset(self)
        self.workflow = WorkflowAsset(self)
        self.jsonform = JsonFormAsset(self)

