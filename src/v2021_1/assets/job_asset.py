# Defines the Job-specific methods organized within the Job class.

import logging
from typing import TYPE_CHECKING, Any, Literal, overload

from src.base import JobAsset, JobModel
from src.exceptions import ApiError
from src.v2021_1.models import JobModel2021_1

if TYPE_CHECKING:
    from src.v2021_1.itential2021_1 import Itential2021_1  # Itential2021_1 imports JobAsset2021_1

log = logging.getLogger(__name__)


class JobAsset2021_1(JobAsset):
    def __init__(self, parent: "Itential2021_1"):
        self.parent = parent

    def retrieve(self, job_id: str) -> "JobModel":
        """
        Get a job by job ID.

        Args:
            job_id (str): The unique job ID. Usually labeled as "_id" in the platform.

        Returns:
            JobModel2021_1: A Job object with the job details except "variables". This is a quirk of the version.

        Notes:
            Use Job.update() if the job isn't completed/canceled/errored to get the full job details.
            Use Job.get_output() to get the job variables.

        """
        response = self.parent.call(method="GET", endpoint=f"/workflow_engine/getJob/{job_id}")

        if response.ok:
            return JobModel2021_1(itential_instance=self.parent, **response.json())
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    def retrieve_lean(
        self, job_id: str, include: list[str] = None, exclude: list[str] = None, **kwargs
    ) -> JobModel2021_1:
        """
        An opinionated method that requires either an 'include' or 'exclude' to limit the response size.

        Args:
            job_id (str): The job_id to retrieve
            include (list[str]): The fields to include in the job object. Exclusive with excludes.
            exclude (list[str]): The fields to exclude in the job object. Exclusive with includes.

        Returns:
            JobModel2021_1: A Job object with only the specified fields filled in.
        """

        if include and exclude:
            raise ValueError("Either 'include' OR 'exclude' arg must be provided, not both.")
        if not include and not exclude:
            raise ValueError("Either 'include' or 'exclude' arg must be provided.")

        query = {"_id": job_id}

        fields = {}
        if include:
            fields = {prop: 1 for prop in include}
        elif exclude:
            fields = {prop: 0 for prop in exclude}

        job_list = self.search(query=query, limit=1, fields=fields, **kwargs)
        if len(job_list) == 1:
            return job_list[0]
        if len(job_list) == 0:
            log.error(f"No job found with id: {job_id}")
            raise ApiError(404, f"Api Error: No job found with id: {job_id} - {job_list}", None)

    @overload
    def search(
        self,
        workflow_name: str,
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
        fields: dict[str, Literal[0, 1]] = None,
    ) -> list[JobModel2021_1]: ...

    @overload
    def search(
        self,
        query: dict[str, Any],
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
        fields: dict[str, Literal[0, 1]] = None,
    ) -> list[JobModel2021_1]: ...

    def search(self, **kwargs) -> list[JobModel2021_1]:
        """
        Get a list of jobs.

        Args:
            query (dict): The query to filter jobs by. Ex: {"name": "workflow_name"}
            get_all: If True, will return all jobs for the workflow. If False, will return the first page of jobs.
            max_amt: The maximum number of jobs to return. If 0, will return all jobs.
            expand (list[str]): The fields to expand in the job object.
            limit: Max results to return per page. Server limit is 100.
            skip: Number to offset the search by
            sort: {"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
            fields: {"name": 1}. "name" field can be any field in the workflow json. Used to filter out other fields

        Examples:
            get_jobs(workflow_name="abcd", limit=50, sort={"name": -1})

            {
              "options": {
                "expand": [
                  "user",
                  "owner",
                  "owner",
                  "user"
                ],
                "fields": {
                  "name": 1
                },
                "query": {
                  "name": "abcd"
                },
                "limit": 50,
                "local": true,
                "skip": 0,
                "sort": {
                  "name": -1
                }
              }
            }
        """

        # Overload section
        query = kwargs.get("query")
        if workflow_name := kwargs.get("workflow_name"):
            query = {"name": workflow_name}

        # Defaults
        get_all = kwargs.get("get_all", False)
        max_amt = kwargs.get("max_amt", 0)
        expand = kwargs.get("expand", ["last_updated_by", "created_by"])
        limit = kwargs.get("limit", 100)
        skip = kwargs.get("skip", 0)
        sort = kwargs.get("sort", {"metrics.start_time": -1})
        fields = kwargs.get(
            "fields",
            {
                "tasks": 0,
                "transitions": 0,
            },
        )

        # Baseline payload query.
        options = {"query": query, "limit": limit, "skip": skip}

        if sort:
            options["sort"] = sort

        if expand:
            options["expand"] = expand

        # Unless the user specifically wants the tasks and transitions, they will be excluded by default.
        if fields:
            options["fields"] = fields

        # Only add the default exclusions if the user is using the fields param to exclude fields.
        # Checking for 0s, since the 'include'/'exclude' args don't make it to this level.
        if not all([value for value in fields.values()]):  # Values have to be all 0 or all 1. No mixing.
            log.debug("Payload only contains exclude fields, adding default exclusions.")
            if "tasks" not in fields:
                options["fields"]["tasks"] = 0
            if "transitions" not in fields:
                options["fields"]["transitions"] = 0
            if "last_updated_by" in expand:  # Trim down the excessive response when expanding this field.
                options["fields"].update(
                    {
                        "last_updated_by.memberOf": 0,  # Required because of default expand fields.
                        "last_updated_by.assignedRoles": 0,  # Required because of default expand fields.
                        "last_updated_by._meta": 0,  # Required because of default expand fields.
                    }
                )
            if "created_by" in expand:  # Trim down the excessive response when expanding this field.
                options["fields"].update(
                    {
                        "created_by.memberOf": 0,  # Required because of default expand fields.
                        "created_by.assignedRoles": 0,  # Required because of default expand fields.
                        "created_by._meta": 0,  # Required because of default expand fields.
                    }
                )

        # Wrap the options in the payload.
        payload = {"options": options}

        log.debug(f"'get_jobs' payload: {payload}")
        response = self.parent.call(method="POST", endpoint="/workflow_engine/jobs/search", json=payload)
        if response.ok:
            response_json = response.json()

            if get_all is True:
                jobs: list[dict] = response_json["results"]

                while response_json["metadata"]["nextPageSkip"] is not None:
                    if max_amt and len(jobs) >= max_amt:
                        break

                    payload["skip"] = response_json["metadata"]["nextPageSkip"]

                    response = self.parent.call(method="POST", endpoint="/workflow_engine/jobs/search", json=payload)
                    response_json = response.json()
                    jobs.extend(response_json["results"])

            else:
                jobs = response_json["results"]

            if max_amt:
                jobs = jobs[:max_amt]

            return [JobModel2021_1(itential_instance=self.parent, **job) for job in jobs]
        else:
            raise ApiError(response.status_code, f"Api Error: {response.reason} - {response.content}", response.json())

    @overload
    def search_lean(
        self,
        workflow_name: str,
        include: list[str] | None = None,
        exclude: list[str] | None = None,
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
    ) -> list[JobModel2021_1]: ...

    @overload
    def search_lean(
        self,
        query: dict[str, Any],
        include: list[str] | None = None,
        exclude: list[str] | None = None,
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
    ) -> list[JobModel2021_1]: ...

    def search_lean(self, **kwargs) -> list[JobModel2021_1]:
        """
        An opinionated method that requires either an 'include' or 'exclude' to limit the response size.

        Args:
            query (dict): The query to filter jobs by. Ex: {"name": "workflow_name"}
            include (list[str]): The fields to include in the job object. Exclusive with excludes.
            exclude (list[str]): The fields to exclude in the job object. Exclusive with includes.

        Returns:
            list[JobModel2021_1]: A list of Job objects with only the specified fields filled in.
        """

        # overload resolution
        if workflow_name := kwargs.get("workflow_name"):
            query = {"name": workflow_name}
        else:
            query = kwargs.get("query")

        include = kwargs.get("include")
        exclude = kwargs.get("exclude")

        if include and exclude:
            raise ValueError("Either 'include' OR 'exclude' arg must be provided, not both.")
        if not include and not exclude:
            raise ValueError("Either 'include' or 'exclude' arg must be provided.")

        fields = {}
        if include:
            fields = {prop: 1 for prop in include}
        elif exclude:
            fields = {prop: 0 for prop in exclude}

        expand = []  # Explicitly set to an empty list to avoid expanding in the lean function.

        job_list = self.search(query=query, expand=expand, fields=fields, **kwargs)
        return job_list

    def output(self, job: JobModel2021_1 | str) -> JobModel2021_1:
        """
        Gets the output of the Job if the job is completed (but not cancelled).
        The platform endpoint only returns a dictionary of job-level variables.

        Args:
            job (JobModel2021_1 | str): The unique job ID. Usually labeled as "_id" in the platform.

        Returns:
            JobModel2021_1: A Job object with only the "id" and "variables" fields filled in.

        Notes:
            Use Job.update() to get the full job details.
        """

        if isinstance(job, JobModel2021_1):
            job_id = job.id
        elif isinstance(job, str):
            job_id = job
        else:
            raise ValueError(f"Invalid job object type: '{type(job)}' Requires: 'str' or 'Job2021_1'")

        response = self.parent.call(method="GET", endpoint=f"/workflow_engine/job/{job_id}/output")
        if response.ok:
            return JobModel2021_1(itential_instance=self.parent, id=job_id, variables=response.json())
        else:
            raise ApiError(response.status_code, f"Api Error: {response.reason} - {response.content}", response.json())
