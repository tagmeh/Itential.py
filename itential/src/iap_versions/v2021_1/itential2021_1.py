import logging
from typing import Any

from itential.src.auth import Auth
from itential.src.iap_versions.v2021_1.assets import JobAsset, JsonFormAsset, WorkflowAsset, Scripts
from itential.src.versions import ItentialVersion

log = logging.getLogger(__name__)


class Itential2021_1(Auth):
    version = ItentialVersion.V2021_1

    def __init__(self, **kwargs: Any):
        log.debug("Initializing Itential 2021.1 class instance.")
        # Imported like this to allow automatic authentication and session handling via the call() method.
        Auth.__init__(self, **kwargs)
        # Import subclasses
        self.scripts = Scripts(self)
        self.job = JobAsset(self)
        self.workflow = WorkflowAsset(self)
        self.jsonform = JsonFormAsset(self)


if __name__ == "__main__":
    itential = Itential2021_1()

    from pathlib import Path

    repo_path = Path(r"\\wsl$\Debian\home\ac08997\IAP-Docker\apps_and_adapters\v2021.1\ctl\app-oaas")

    itential.scripts.import_repo(repo_path=repo_path)
