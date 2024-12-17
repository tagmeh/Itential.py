import logging


from itential2.src import endpoints
from itential2.src.asset_classes.job_versions import Job
from itential2.src.core import Core
from itential2.src.versions import SupportedVersion

logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)


class Itential(Core):
    def __init__(self, username: str, password: str, version: SupportedVersion, url: str = "http://localhost:3000", **kwargs):
        self.version = version
        super().__init__(username=username, password=password, url=url, **kwargs)

    def get_job(self, job_id: str) -> Job:
        return endpoints.get_job(self, job_id=job_id)


if __name__ == '__main__':
    # url = r"https://autopilot-prod.corp.intranet:443"
    username = "admin@pronghorn"
    password = "admin"

    itential = Itential(username=username, password=password, version=SupportedVersion.V2021_1)
    print(itential.url)

    jerb = itential.get_job("3a27928f699e4658b4df5aeb")
    print(jerb)
    print(jerb.status)

