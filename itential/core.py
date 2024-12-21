import logging
from abc import ABC, abstractmethod
from typing import Any

from itential.src.iap_versions.base import Job, Workflow
from itential.src.versions import ItentialVersion

log = logging.getLogger(__name__)


class Itential(ABC):
    _version_map = {
        ItentialVersion.V2021_1: "itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1",
        ItentialVersion.V2023_1: "itential.src.iap_versions.v2023_1.itential2023_1.Itential2023_1",
    }

    @classmethod
    def create(
        cls,
        version: ItentialVersion,
        username: str = "admin@pronghorn",
        password: str = "admin",
        url: str = "http://localhost:3000",
    ):
        if cls.__name__ != 'Itential':
            raise NotImplementedError(".create() is not available from the subclass.")

        log.debug(f'Creating version-specific Itential instance with version: {version.value}')
        module_path, class_name = Itential._version_map[version].rsplit(".", 1)
        log.debug(f"Preparing to import '{class_name}' from '{module_path}'")

        module = __import__(module_path, fromlist=[class_name])

        log.debug(f"Imported '{class_name}'")
        versioned_class = getattr(module, class_name)
        return versioned_class(username=username, password=password, url=url)

    @abstractmethod
    def get_job(self, job_id: str) -> Job: ...

    @abstractmethod
    def get_jobs(self, **kwargs: dict[str, Any]) -> list[Job]: ...

    @abstractmethod
    def get_job_output(self, **kwargs: dict[str, Any]) -> Job: ...

    @abstractmethod
    def get_workflow(self, **kwargs: dict[str, Any]) -> Workflow: ...

    @abstractmethod
    def get_workflows(self, **kwargs: dict[str, Any]) -> list[Workflow]: ...

    @abstractmethod
    def export_workflow(self, **kwargs: dict[str, Any]) -> Workflow: ...


def main() -> None:
    urllib3_logger = logging.getLogger("urllib3")
    urllib3_logger.setLevel(logging.WARNING)

    username = "admin@pronghorn"
    password = "admin"

    i = Itential.create(version=ItentialVersion.V2021_1)
    print(i)
    print(type(i))

    # itential_2021 = Itential(username=username, password=password, version=ItentialVersion.V2021_1)
    #
    # jobs = itential_2021.get_jobs()
    #
    # lean_jerb = itential_2021.get_lean_job(
    #     "3a27928f699e4658b4df5aeb", includes=["_id", "name", "status", "metrics.start_time"]
    # )
    # print(f'{lean_jerb.id=}')
    # print(f'{lean_jerb.name=}')
    # print(f'{lean_jerb.metrics.start_time=}')
    # print(f'{lean_jerb.status=}')
    # print(f'{lean_jerb.variables=}')
    # print(f'{lean_jerb.canvas_version=}')
    # print(f'{lean_jerb.transitions=}')

    #
    # jerb = itential_2021.get_job("3a27928f699e4658b4df5aeb")
    # print(jerb.id)
    # print(type(jerb))
    # # pprint(jerb.model_dump(mode='python'))
    # print(jerb.status)
    #
    # completed_jerb = itential_2021.get_job("a479e9ea13334b6999fc0efb")
    # print(completed_jerb.name)
    # print(completed_jerb.variables)
    # completed_jerb.get_output()
    # print(completed_jerb.variables)
    # print(completed_jerb.status)
    # print(completed_jerb.update())
    #
    # completed_jerb_output_only = itential_2021.get_job_output("a479e9ea13334b6999fc0efb")
    # print(completed_jerb_output_only)
    #
    # errored_job = itential_2021.get_job("cd9361acfa724ba49f3e808c")
    # print(errored_job.name)
    # print(f"{errored_job.error=}")
    # print(errored_job.status)
    # print(errored_job.get_output())
    # # print(errored_job.model_dump(mode='python'))
    #
    # cancelled_job = itential_2021.get_job("3a27928f699e4658b4df5aeb")
    # print(f"{cancelled_job.error=}")
    # print(cancelled_job.get_output())
    #
    # werkflow = itential_2021.get_workflow("Test_Rate_Limited_ChildJob_Task")
    # print(werkflow.name)
    # print(type(werkflow))
    # # pprint(werkflow.model_dump(mode='python'))
    #
    # exported_werkflow = itential_2021.export_workflow("Test_Rate_Limited_ChildJob_Task")
    # print(exported_werkflow.name)
    # print(type(exported_werkflow))
    # # pprint(exported_werkflow.model_dump(mode='python'))
    #
    # jerbs = itential_2021.get_jobs("Test_Rate_Limited_ChildJob_Task", all_jobs=False, limit=100,
    #                                fields={"_id": 1, "name": 1, "metrics.start_time": 1})
    # print(len(jerbs))
    # print(type(jerbs))
    #
    # jerbs_from_werkflow = werkflow.get_jobs(limit=20)
    # print(len(jerbs_from_werkflow))

    # itential_2023 = Itential(username=username, password=password, version=ItentialVersion.V2023_1)

    # # Query for a specific job given a job_id.
    # jerb = itential_2023.get_job("2eb6d0afb569405d9b165f20")
    # print(f"{jerb.name=}")
    # print(f"{jerb.id=}")
    # print(f"{type(jerb)=}")
    #
    # # Use the job to get it's associated workflow.
    # jerb_werkflow = jerb.get_workflow()
    # print(f"{jerb_werkflow.name=}")
    # print(f"{jerb_werkflow.id=}")
    # print(f"{type(jerb_werkflow)=}")
    #
    # jerbs = itential_2023.get_jobs("Color Timer Workflow", all_jobs=False, limit=100, include="_id,name,metrics.start_time")
    # print(f"{type(jerbs)=}")
    # print(f"{len(jerbs)=}")
    # if isinstance(jerbs, str):
    #     print(f"{jerbs=}")
    # print(f"{jerbs[0]=}")
    #
    # jerbs_from_werkflow = jerb_werkflow.get_jobs(limit=20)
    # print(len(jerbs_from_werkflow))
    #
    # werkflow = itential_2023.get_workflow("Color Timer Workflow")
    # pprint(werkflow.model_dump(mode='python'))
    # print(werkflow.id)

    # completed_jerb = itential_2023.get_job("5905c7e1d1a242debf713c24")
    # print(completed_jerb.status)
    # print(completed_jerb.variables)
    # completed_jerb.update()
    #
    #
    # cancelled_jerb = itential_2023.get_job("902092e27f8345abb7c1305c")
    # print(cancelled_jerb.status)
    # print(completed_jerb.variables)
    # cancelled_jerb.update()
    #
    #
    # errored_jerb = itential_2023.get_job("5f31f24cf2a441cfa6bcbe04")
    # print(errored_jerb.status)
    # print(completed_jerb.variables)
    # errored_jerb.update()
    #
    # completed_jerb2 = itential_2023.get_job_output("5905c7e1d1a242debf713c24")  # Should print warning, doesnt.

    # werkflow.run(payload)
    # werkflow.import()  # Imports into the IAP instance
    # werkflow.save()
    # werkflow.get_jobs()

    # exported_werkflow = itential_2023.export_workflow("Color Timer Workflow")
    # pprint(exported_werkflow.model_dump(mode='python'))
    # exported_werkflow.get_jobs()


if __name__ == '__main__':
    main()
