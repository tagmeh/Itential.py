import logging


from itential2.src import endpoints
from itential2.src.asset_classes.asset_versions import Job
from itential2.src.core import Core
from itential2.src.versions import SupportedVersion


logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)


class Itential(Core):
    def __init__(
        self, username: str, password: str, version: SupportedVersion, url: str = "http://localhost:3000", **kwargs
    ):
        self.version = version
        super().__init__(username=username, password=password, url=url, **kwargs)

    def get_job(self, job_id: str) -> Job:
        return endpoints.get_job(self, job_id=job_id)

    def get_workflow(self, workflow_name: str):
        return endpoints.get_workflow(self, workflow_name=workflow_name)

    def export_workflow(self, workflow_name: str):
        return endpoints.export_workflow(self, workflow_name=workflow_name)


if __name__ == '__main__':
    # url = r"https://autopilot-prod.corp.intranet:443"
    username = "admin@pronghorn"
    password = "admin"

    itential = Itential(username=username, password=password, version=SupportedVersion.V2021_1)

    from pprint import pprint

    #
    # jerb = itential.get_job("3a27928f699e4658b4df5aeb")
    # pprint(jerb.model_dump(mode='python'))
    #
    # werkflow = itential.get_workflow("Test_Rate_Limited_ChildJob_Task")
    # pprint(werkflow.model_dump(mode='python'))
    #
    # exported_werkflow = itential.export_workflow("Test_Rate_Limited_ChildJob_Task")
    # pprint(exported_werkflow.model_dump(mode='python'))

    itential_2023 = Itential(username=username, password=password, version=SupportedVersion.V2023_1)

    jerb = itential_2023.get_job("2eb6d0afb569405d9b165f20")
    pprint(jerb.model_dump(mode='python'))

    werkflow = itential_2023.get_workflow("Color Timer Workflow")
    pprint(werkflow.model_dump(mode='python'))

    exported_werkflow = itential_2023.export_workflow("Color Timer Workflow")
    pprint(exported_werkflow.model_dump(mode='python'))

    # {'ancestors': ['3a27928f699e4658b4df5aeb'],
    #  'canvas_version': None,
    #  'created': datetime.datetime(2024, 12, 13, 17, 28, 51, 508000, tzinfo=TzInfo(UTC)),
    #  'created_by': '675c9be151810d0032df1c47',
    #  'created_version': None,
    #  'decorators': [],
    #  'description': '',
    #  'groups': ['default'],
    #  'last_updated': datetime.datetime(2024, 12, 13, 21, 20, 21, 319000, tzinfo=TzInfo(UTC)),
    #  'last_updated_by': '675c936a13675f000b815be4',
    #  'last_updated_version': None,
    #  'metrics': Metrics(start_time=datetime.datetime(2024, 12, 13, 21, 20, 21, 250000, tzinfo=TzInfo(UTC)),
    #                     user='675c936a13675f000b815be4', progress=0.75, end_time=None),
    #  'name': 'Test_Rate_Limited_ChildJob_Task',
    #  'parent': None,
    #  'pre_automation_time': None,
    #  'sla': None,
    #  'status': 'error',
    #  'variables': None,
    #  'watchers': ['675c936a13675f000b815be4']}
