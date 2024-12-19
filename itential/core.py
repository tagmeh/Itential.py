import logging
from typing import Any, Literal

from itential import src
from itential.src.auth import AuthBase
from itential.src.iap_versions.base.models import Job, Workflow
from itential.src.versions import ItentialVersion

log = logging.getLogger(__name__)


class Itential(AuthBase):
    def __init__(
        self,
        version: ItentialVersion,
        username: str = "admin@pronghorn",
        password: str = "admin",
        url: str = "http://localhost:3000",
        **kwargs: Any,
    ):
        self.version = version
        log.debug(f"Creating Itential instance for version {version}")
        super().__init__(username=username, password=password, url=url, **kwargs)

    def get_job(self, job_id: str) -> Job:
        return src.get_job(self, job_id=job_id)

    def get_lean_job(
        self, job_id: str, includes: list[str] | None = None, excludes: list[str] | None = None, **kwargs
    ) -> Job | None:
        """
        Returns a Job object with only the specified fields filled in.
        A hard-coded query should limit the number of jobs found to between 0 and 1.
        """

        if not includes and not excludes:
            raise ValueError("Either includes or excludes must be provided.")

        return src.get_lean_job(self, job_id=job_id, includes=includes, excludes=excludes, **kwargs)

    def get_jobs_by_workflow_name(self, workflow_name: str, **kwargs: Any) -> list[Job]:
        query = {"name": workflow_name}
        return self.get_jobs(query=query, **kwargs)

    def get_jobs(
        self,
        query: dict[str, Any],
        all_jobs: bool = False,
        max_jobs: int | None = None,
        limit: int = 100,
        includes: list[str] | None = None,
        excludes: list[str] | None = None,
        skip: int = 0,
        sort: str | None = None,
        order: Literal[1, -1] = None,
        expand: list[str] | None = None,
    ) -> list[Job]:
        """
        Returns a list of Job objects based on the provided search criteria.

        Args:
            query (dict[str, Any]): A dictionary of fields and values to search for. Ignored if 'workflow_name' is provided.
            all_jobs (bool): If True, will return all jobs for the workflow. If False, will return the first page of jobs.
            max_jobs (bool): Allows for a partial list of jobs to be returned. 'all_jobs' will override this.
            limit (int): Max results to return per page. Server limit is 100.
            includes (list[str]): Translates into {"field": {"include": 1, "fields": 1}}. Mutually exclusive with 'excludes'
            excludes (list[str]): Translates into {"field": {"include": 0, "fields": 0}}. Mutually exclusive with 'includes'
            skip (int): Number to offset the search by.
            sort (str): The field to sort by. Required if 'order' is provided.
            order (Literal[1, -1]): The order to sort by. 1 for ascending, -1 for descending. Required if 'sort' is provided.
            expand (list[str]): A list of fields to return the full object for. Useful for user objects.

        Notes:
            'workflow_name' is an opinionated search field. It generates an exact string match query.
            Use 'query' if you need a more complex search. (And don't pass in 'workflow_name').
            'includes' and 'excludes' are mutually exclusive.
            'sort' and 'order' are both required if either are provided.

        Returns: list[Job]: A list of Job objects based on the provided search criteria.

        """

        if includes and excludes:
            raise ValueError("'includes' and 'excludes' are mutually exclusive.")

        if any([sort, order]) and not all([sort, order]):
            raise ValueError("'sort' and 'order' must both be provided if either is provided.")

        if all_jobs and max_jobs:
            log.warning("'all_jobs' and 'max_jobs' provided. 'all_jobs' will override 'max_jobs'.")

        return src.get_jobs(
            self,
            all_jobs=all_jobs,
            max_jobs=max_jobs,
            limit=limit,
            includes=includes,
            excludes=excludes,
            skip=skip,
            sort=sort,
            order=order,
            expand=expand,
            query=query,
        )

    def get_lean_jobs(
        self,
        query: dict[str, Any],
        includes: list[str] | None = None,
        excludes: list[str] | None = None,
        **kwargs,
    ) -> list[Job]:
        """
        An opinionated wrapper around the "get_jobs" method.
        Enforces the usage of 'includes' or 'excludes' to limit the fields returned for each job.
        Returns a list of Job objects with only the specified fields filled in.
        """

        if not includes and not excludes:
            raise ValueError("Either includes or excludes must be provided.")

        return self.get_jobs(query=query, includes=includes, excludes=excludes, **kwargs)

    def get_job_output(self, job_id: str):
        return src.get_job_output(self, job_id=job_id)

    def get_workflow(self, workflow_name: str) -> Workflow:
        return src.get_workflow(self, workflow_name=workflow_name)

    def export_workflow(self, workflow_name: str) -> Workflow:
        return src.export_workflow(self, workflow_name=workflow_name)


def main() -> None:
    urllib3_logger = logging.getLogger("urllib3")
    urllib3_logger.setLevel(logging.WARNING)

    username = "admin@pronghorn"
    password = "admin"

    itential_2021 = Itential(username=username, password=password, version=ItentialVersion.V2021_1)

    jobs = itential_2021.get_jobs()


    lean_jerb = itential_2021.get_lean_job(
        "3a27928f699e4658b4df5aeb", includes=["_id", "name", "status", "metrics.start_time"]
    )
    print(f'{lean_jerb.id=}')
    print(f'{lean_jerb.name=}')
    print(f'{lean_jerb.metrics.start_time=}')
    print(f'{lean_jerb.status=}')
    print(f'{lean_jerb.variables=}')
    print(f'{lean_jerb.canvas_version=}')
    print(f'{lean_jerb.transitions=}')

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
