import logging
from typing import Any

from src.base.itential import Itential
from src.v2021_1.assets.job_asset import JobAsset
from src.v2021_1.assets.workflow_asset import WorkflowAsset

# from src.v2021_1.asset_classes.jsonform_asset import JsonFormAsset
# from src.v2021_1.asset_classes.scripts import Scripts
from src.versions import ItentialVersion

log = logging.getLogger(__name__)


class Itential2021_1(Itential):
    version = ItentialVersion.V2021_1

    def __init__(self, username: str, password: str, server_url: str, **kwargs: Any):
        log.debug("Initializing Itential parent class instance.")
        super().__init__(username=username, password=password, server_url=server_url, **kwargs)

        # Import subclasses
        log.debug("Initializing Itential 2021.1 subclasses.")
        # self.scripts = Scripts(self)
        self.job = JobAsset(self)
        self.workflow = WorkflowAsset(self)
        # self.jsonform = JsonFormAsset(self)
