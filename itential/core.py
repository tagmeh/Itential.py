import logging
from typing import Any

from itential import src
from itential.src.auth import AuthBase
from itential.src.iap_versions.base.models import Job, Workflow
from itential.src.versions import ItentialVersion


logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)


class Itential(AuthBase):
    def __init__(
            self,
            version: ItentialVersion,
            username: str = "admin@pronghorn",
            password: str = "admin",
            url: str = "http://localhost:3000",
            **kwargs: Any
    ):
        self.version = version
        super().__init__(username=username, password=password, url=url, **kwargs)

    def get_job(self, job_id: str) -> Job:
        return src.get_job(self, job_id=job_id)

    def get_jobs(self, workflow_name: str, all_jobs: bool = False, limit: int = 10, **kwargs: Any) -> list[Job]:
        return src.get_jobs(self, workflow_name=workflow_name, all_jobs=all_jobs, limit=limit, **kwargs)

    def get_job_output(self, job_id: str):
        return src.get_job_output(self, job_id=job_id)

    def get_workflow(self, workflow_name: str) -> Workflow:
        return src.get_workflow(self, workflow_name=workflow_name)

    def export_workflow(self, workflow_name: str) -> Workflow:
        return src.export_workflow(self, workflow_name=workflow_name)


def main() -> None:
    username = "admin@pronghorn"
    password = "admin"

    itential_2021 = Itential(username=username, password=password, version=ItentialVersion.V2021_1)

    jerb = itential_2021.get_job("3a27928f699e4658b4df5aeb")
    print(jerb.id)
    print(type(jerb))
    # pprint(jerb.model_dump(mode='python'))
    print(jerb.status)

    completed_jerb = itential_2021.get_job("a479e9ea13334b6999fc0efb")
    print(completed_jerb.name)
    print(completed_jerb.variables)
    completed_jerb.get_output()
    print(completed_jerb.variables)
    print(completed_jerb.status)
    print(completed_jerb.update())

    completed_jerb_output_only = itential_2021.get_job_output("a479e9ea13334b6999fc0efb")
    print(completed_jerb_output_only)

    errored_job = itential_2021.get_job("cd9361acfa724ba49f3e808c")
    print(errored_job.name)
    print(f"{errored_job.error=}")
    print(errored_job.status)
    print(errored_job.get_output())
    # print(errored_job.model_dump(mode='python'))

    cancelled_job = itential_2021.get_job("3a27928f699e4658b4df5aeb")
    print(f"{cancelled_job.error=}")
    print(cancelled_job.get_output())

    werkflow = itential_2021.get_workflow("Test_Rate_Limited_ChildJob_Task")
    print(werkflow.name)
    print(type(werkflow))
    # pprint(werkflow.model_dump(mode='python'))

    exported_werkflow = itential_2021.export_workflow("Test_Rate_Limited_ChildJob_Task")
    print(exported_werkflow.name)
    print(type(exported_werkflow))
    # pprint(exported_werkflow.model_dump(mode='python'))

    jerbs = itential_2021.get_jobs("Test_Rate_Limited_ChildJob_Task", all_jobs=False, limit=100,
                                   fields={"_id": 1, "name": 1, "metrics.start_time": 1})
    print(len(jerbs))
    print(type(jerbs))

    jerbs_from_werkflow = werkflow.get_jobs(limit=20)
    print(len(jerbs_from_werkflow))


    # itential_2023 = Itential(username=username, password=password, version=ItentialVersion.V2023_1)

    # Query for a specific job given a job_id.
    # jerb = itential_2023.get_job("2eb6d0afb569405d9b165f20")
    # print(f"{jerb.name=}")
    # print(f"{jerb.id=}")
    # print(f"{type(jerb)=}")
    #
    # Use the job to get it's associated workflow.
    # jerb_werkflow = jerb.get_workflow()
    # print(f"{jerb_werkflow.name=}")
    # print(f"{jerb_werkflow.id=}")
    # print(f"{type(jerb_werkflow)=}")

    # jerbs = itential_2023.get_jobs("Color Timer Workflow", all_jobs=False, limit=100, include="_id,name,metrics.start_time")
    # print(f"{type(jerbs)=}")
    # print(f"{len(jerbs)=}")
    # if isinstance(jerbs, str):
    #     print(f"{jerbs=}")
    # print(f"{jerbs[0]=}")

    # jerbs_from_werkflow = jerb_werkflow.get_jobs(limit=20)
    # print(len(jerbs_from_werkflow))

    # werkflow = itential_2023.get_workflow("Color Timer Workflow")
    # pprint(werkflow.model_dump(mode='python'))
    # print(werkflow.id)

    # werkflow.run(payload)
    # werkflow.import()  # Imports into the IAP instance
    # werkflow.save()
    # werkflow.get_jobs()

    # exported_werkflow = itential_2023.export_workflow("Color Timer Workflow")
    # pprint(exported_werkflow.model_dump(mode='python'))
    # exported_werkflow.get_jobs()


if __name__ == '__main__':
    main()
