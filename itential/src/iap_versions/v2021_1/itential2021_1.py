import logging
from typing import Any, Literal, overload, Union

from itential.src.auth import Auth
from itential.src.exceptions import ApiError
from itential.src.iap_versions.base.wrappers import inject_itential_instance
from itential.src.iap_versions.v2021_1.models.job2021_1 import Job2021_1
from itential.src.iap_versions.v2021_1.models.workflow2021_1 import Workflow2021_1
from itential.src.versions import ItentialVersion

log = logging.getLogger(__name__)


class Itential2021_1(Auth):
    version = ItentialVersion.V2021_1

    def __init__(self, **kwargs: Any):
        log.debug("Initializing Itential 2021.1 class instance.")
        Auth.__init__(self, **kwargs)  # Authentication for the Itential server

    @inject_itential_instance
    def get_job(self, job_id: str) -> Job2021_1:
        """
        Get a job by job ID.

        Args:
            job_id (str): The unique job ID. Usually labeled as "_id" in the platform.

        Returns:
            Job2021_1: A Job object with the job details except "variables". This is a quirk of the version.

        Notes:
            Use Job.update() if the job isn't completed/canceled/errored to get the full job details.
            Use Job.get_output() to get the job variables.

        """
        response = self.call(method="GET", endpoint=f"/workflow_engine/getJob/{job_id}")
        if response.ok:
            return Job2021_1(**response.json())
        else:
            raise ApiError(
                response.status_code, f"Api Error: {response.reason} - {response.content!r}", response.json()
            )

    @inject_itential_instance
    def get_lean_job(self, job_id: str, include: list[str] = None, exclude: list[str] = None, **kwargs) -> Job2021_1:
        """
        An opinionated method that requires either an 'include' or 'exclude' to limit the response size.

        Args:
            job_id (str): The job_id to retrieve
            include (list[str]): The fields to include in the job object. Exclusive with excludes.
            exclude (list[str]): The fields to exclude in the job object. Exclusive with includes.

        Returns:
            Job2021_1: A Job object with only the specified fields filled in.
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

        job_list = self.get_jobs(query=query, limit=1, fields=fields, **kwargs)
        if len(job_list) == 1:
            return job_list[0]
        if len(job_list) == 0:
            log.error(f"No job found with id: {job_id}")
            raise ApiError(404, f"Api Error: No job found with id: {job_id} - {job_list}", None)

    @overload
    def get_jobs(
        self,
        workflow_name: str,
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
        fields: dict[str, Literal[0, 1]] = None,
    ) -> list[Job2021_1]: ...

    @overload
    def get_jobs(
        self,
        query: dict[str, Any],
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
        fields: dict[str, Literal[0, 1]] = None,
    ) -> list[Job2021_1]: ...

    @inject_itential_instance
    def get_jobs(self, **kwargs) -> list[Job2021_1]:
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
        response = self.call(method="POST", endpoint="/workflow_engine/jobs/search", json=payload)
        if response.ok:
            response_json = response.json()

            if get_all is True:
                jobs: list[dict] = response_json["results"]

                while response_json["metadata"]["nextPageSkip"] is not None:
                    if max_amt and len(jobs) >= max_amt:
                        break

                    payload["skip"] = response_json["metadata"]["nextPageSkip"]

                    response = self.call(method="POST", endpoint="/workflow_engine/jobs/search", json=payload)
                    response_json = response.json()
                    jobs.extend(response_json["results"])

            else:
                jobs = response_json["results"]

            if max_amt:
                jobs = jobs[:max_amt]

            return [Job2021_1(**job) for job in jobs]
        else:
            raise ApiError(response.status_code, f"Api Error: {response.reason} - {response.content}", response.json())

    @inject_itential_instance
    def get_job_output(self, job: Job2021_1 | str) -> Job2021_1:
        """
        Gets the output of the Job if the job is completed (but not cancelled).
        The platform endpoint only returns a dictionary of job-level variables.

        Args:
            job_id (str): The unique job ID. Usually labeled as "_id" in the platform.

        Returns:
            Job2021_1: A Job object with only the "id" and "variables" fields filled in.

        Notes:
            Use Job.update() to get the full job details.
        """

        if isinstance(job, Job2021_1):
            job_id = job.id
        elif isinstance(job, str):
            job_id = job
        else:
            raise ValueError(f"Invalid job object type: '{type(job)}' Requires: 'str' or 'Job2021_1'")

        response = self.call(method="GET", endpoint=f"/workflow_engine/job/{job_id}/output")
        if response.ok:
            return Job2021_1(id=job_id, variables=response.json())
        else:
            raise ApiError(response.status_code, f"Api Error: {response.reason} - {response.content}", response.json())

    @overload
    def get_lean_jobs(
        self,
        workflow_name: str,
        include: list[str] = None,
        exclude: list[str] = None,
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
    ) -> list[Job2021_1]: ...

    @overload
    def get_lean_jobs(
        self,
        query: dict[str, Any],
        include: list[str] = None,
        exclude: list[str] = None,
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
    ) -> list[Job2021_1]: ...

    @inject_itential_instance
    def get_lean_jobs(self, **kwargs) -> list[Job2021_1]:
        """
        An opinionated method that requires either an 'include' or 'exclude' to limit the response size.

        Args:
            query (dict): The query to filter jobs by. Ex: {"name": "workflow_name"}
            include (list[str]): The fields to include in the job object. Exclusive with excludes.
            exclude (list[str]): The fields to exclude in the job object. Exclusive with includes.
            kwargs (dict): Additional query parameters to pass to get_jobs_by_query

        Returns:
            list[Job2021_1]: A list of Job objects with only the specified fields filled in.
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

        job_list = self.get_jobs(query=query, expand=expand, fields=fields, **kwargs)
        return job_list

    @overload
    def get_workflow(self, workflow_name: str, expand: list[str] = None) -> Workflow2021_1:
        """
        Uses a static payload with the workflow_engine/workflows/search endpoint.

        Args:
            workflow_name (str): The name of the workflow to retrieve.
            expand (list[str]): The fields to expand in the workflow object.

        Returns:
            Workflow2021_1: A Workflow object with the workflow details.
        """
        ...

    @overload
    def get_workflow(self, query: dict[str, Any], expand: list[str] = None, **kwargs) -> Workflow2021_1: ...

    @overload
    def get_workflow(self, job: Job2021_1, expand: list[str] = None, **kwargs) -> Workflow2021_1:
        """
        Get the workflow associated with a job.

        Args:
            job (Job2021_1): The job object used to retrieve the associated workflow.
            expand (list[str]): The fields to expand in the workflow object.
            kwargs (dict): Additional query parameters to pass to get_workflows_by_query

        Returns:
            Workflow2021_1: A Workflow object with the workflow details.
        """
        ...

    @overload
    def get_workflow(self, job_id: int, expand: list[str] = None, **kwargs): ...

    @inject_itential_instance
    def get_workflow(self, **kwargs) -> Workflow2021_1 | None:
        """
        Opinionated workflows/search endpoint query method that only returns one workflow.

        Args:
            query (dict): The query to filter workflows by. Ex: {"name": "workflow_name"}
            expand (list[str]): The fields to expand in the workflow object.
            kwargs (dict): Additional query parameters to pass to get_workflows_by_query

        Returns:
            Workflow2021_1: A Workflow object with the workflow details.
        """

        # overload resolution
        if workflow_name := kwargs.get("workflow_name"):
            query = {"name": workflow_name}
        elif job := kwargs.get("job"):
            query = {"name": job.name}
        elif job_id := kwargs.get("job_id"):
            query = {"name": job_id}
        else:
            query = kwargs.get("query")
            del kwargs["query"]

        workflow_list = self.get_workflows(query=query, limit=1, **kwargs)
        if len(workflow_list) == 1:
            return workflow_list[0]
        if len(workflow_list) == 0:
            log.error(f"No workflow found with query: {query}")
            return None

    @inject_itential_instance
    def get_lean_workflow(
        self, workflow_name: str, include: list[str] = None, exclude: list[str] = None
    ) -> Workflow2021_1 | None:
        """
        An opinionated method that requires either an 'include' or 'exclude' to limit the response size.

        Args:
            workflow_name (str): The name of the workflow to retrieve.
            include (list[str]): The fields to include in the workflow object. Exclusive with excludes.
            exclude (list[str]): The fields to exclude in the workflow object. Exclusive with includes.

        Returns:
            Workflow2021_1: A Workflow object with only the specified fields filled in.
        """

        if include and exclude:
            raise ValueError("Either include or exclude must be provided, not both.")
        if not include and not exclude:
            raise ValueError("Either include or exclude must be provided.")

        query = {"name": workflow_name}

        fields = {}
        if include:
            include.append("name")  # Always include the name field. We know the name, since it's passed in.
            fields = {prop: 1 for prop in include}
        elif exclude:
            fields = {prop: 0 for prop in exclude}

        expand = []  # Explicitly set to an empty list to avoid expanding in the lean function.

        workflow_list = self.get_workflows(query=query, fields=fields, limit=1, expand=expand)
        if len(workflow_list) == 1:
            return workflow_list[0]
        if len(workflow_list) == 0:
            log.error(f"No workflow found with name: {workflow_name}")
            return None

    @overload
    def get_workflows(
        self,
        workflow_name: str,
        get_all: bool = False,
        max_amt: int = None,
        expand: list[str] = None,
        limit: int = 1,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
        fields: dict[str, Literal[0, 1]] = None,
    ) -> list[Workflow2021_1]:
        """
        Uses a static payload with the workflow_engine/workflows/search endpoint.

        Args:
            workflow_name (str): The names of the workflows to retrieve.
            get_all (bool): If True, will return all workflows for the query. If False, will return the first page of workflows.
            max_amt (int): The maximum number of workflows to return. If None, will return all workflows.
            expand (list[str]): The fields to expand in the workflow object.
            limit (int): Max results to return per page. Server limit is 100.
            skip (int): Number to offset the search by
            sort (dict[str, Literal[1, -1]]): {"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
            fields (dict[str, Literal[0, 1]]): {"name": 1}. "name" field can be any field in the workflow json. Used to filter out other fields

        Returns:
            list[Workflow2021_1]: A list of Workflow objects with the workflow details.
        """
        ...

    @overload
    def get_workflows(
        self,
        query: dict[str, Any],
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 1,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
        fields: dict[str, Literal[0, 1]] = None,
    ) -> list[Workflow2021_1]: ...

    @inject_itential_instance
    def get_workflows(self, **kwargs) -> list[Workflow2021_1]:
        """
        Get a list of workflows.

        Args:
            query (dict): The query to filter workflows by. Ex: {"name": "workflow_name"}
            get_all (bool): If True, will return all workflows for the query. If False, will return the first page of workflows.
            max_amt (int): The maximum number of workflows to return. If 0, will return all workflows.
            expand (list[str]): The fields to expand in the workflow object.
            limit (int): Max results to return per page. Server limit is 100.
            skip (int): Number to offset the search by
            sort (dict[str, Literal[1, -1]): {"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
            fields (dict[str, Literal[0, 1]]): {"name": 1}. "name" field can be any field in the workflow json. Used to filter out other fields

        Returns:
            list[Workflow2021_1]: A list of Workflow objects with the workflow details.
        """

        # Overload resolution
        if workflow_name := kwargs.get("workflow_name"):
            query = {"name": workflow_name}
        else:
            query = kwargs.get("query")

        # Defaults
        get_all = kwargs.get("get_all", False)
        max_amt = kwargs.get("max_amt", 0)
        expand = kwargs.get("expand", ["last_updated_by", "created_by"])
        limit = kwargs.get("limit", 100)
        skip = kwargs.get("skip", 0)
        sort = kwargs.get("sort", {"metrics.start_time": -1})
        fields = kwargs.get(
            "fields",
            {"tasks": 0, "transitions": 0},
        )

        options = {"query": query, "limit": limit, "skip": skip}
        if expand:
            options["expand"] = expand

        if sort:
            options["sort"] = sort

        if limit == 1:
            del options["sort"]  # Nothing to sort in a 1 result query. This is for the singular get_*_workflow methods

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

        payload = {"options": options}

        response = self.call(method="POST", endpoint="/workflow_engine/workflows/search", json=payload)
        if response.ok:
            response_json = response.json()

            if get_all is True:
                workflows = response_json["results"]

                while response_json["metadata"]["nextPageSkip"] is not None:
                    if max_amt and len(workflows) >= max_amt:
                        break

                    payload["skip"] = response_json["metadata"]["nextPageSkip"]
                    response = self.call(method="POST", endpoint="/workflow_engine/workflows/search", json=payload)
                    response_json = response.json()
                    workflows.extend(response_json["results"])

            else:
                workflows = response_json["results"]

            if max_amt:
                workflows = workflows[:max_amt]

            return [Workflow2021_1(**workflow) for workflow in workflows]
        else:
            raise ApiError(response.status_code, f"Api Error: {response.reason} - {response.content}", response.json())

    @inject_itential_instance
    def export_workflow(self, workflow_name: str) -> Workflow2021_1:
        """
        Export a single workflow.

        Args:
            workflow_name (str): The name of the workflow to export.

        Returns:
            Workflow2021_1: A Workflow object with the workflow details.
        """
        payload = {"options": {"name": workflow_name, "type": "automation"}}
        response = self.call(method="POST", endpoint="/workflow_builder/export", json=payload)
        if response.ok:
            return Workflow2021_1(**response.json())
        else:
            raise ApiError(response.status_code, f"Api Error: {response.reason} - {response.content}", response.json())

    def import_workflow(self, workflow: dict | Workflow2021_1, canvas_version: Literal[1, 2] = 1) -> dict | str:
        """
        Import a workflow into the Itential platform. Due to how the 2021.1 platform works, the workflow cannot be
            updated in-place, but instead must be deleted and re-imported.

        An imported workflow must contain a canvasVersion value of 1 or 2. The default is 1 as it's the most
            pushed/documented workflow version.

        The exported/searched workflows do not contain the canvasVersion field for some reason, so it must be
            added to the workflow object before importing.

        Args:
            workflow: Dict or Workflow2021_1 object to import.
            canvas_version: Literal[1, 2]: The canvas version of the workflow. Default is 1.

        Returns:
            str: The name of the workflow that was imported.

        """
        # Step 1: Get workflow object to import.
        if isinstance(workflow, Workflow2021_1):
            workflow_obj = workflow.model_dump_to_import()

        elif isinstance(workflow, dict):
            # Convert to the pydantic model, then output the json for Itential import.
            # Removes fields that can't be imported.
            workflow_obj = Workflow2021_1(**workflow).model_dump_to_import()

        else:
            raise ValueError(f"Invalid workflow object type: {type(workflow)}")

        if workflow_obj.get("canvasVersion") is None:
            workflow_obj["canvasVersion"] = canvas_version

        payload = {"workflow": workflow_obj}

        # Step 2: Verify the workflow doesn't already exist on the platform
        exported_workflow = self.export_workflow(workflow_name=workflow_obj["name"])
        if isinstance(exported_workflow, Workflow2021_1):
            log.debug("Workflow already exists on the platform. Deleting the existing workflow.")
            self.delete_workflow(workflow=exported_workflow.name)

        try:
            # Step 3: Import the workflow
            response = self.call(method="POST", endpoint="/workflow_builder/import", json=payload)
            if response.ok:
                return response.json()["name"]
            else:
                raise ApiError(
                    response.status_code, f"Api Error: {response.reason} - {response.content}", response.json()
                )
        except ApiError as e:
            # Step 4: If the import fails, attempt to re-import the original workflow.
            log.error(f"Failed to import workflow. Attempting to re-import the original workflow.")
            if exported_workflow.canvas_version is None:
                exported_workflow.canvas_version = canvas_version
            self.import_workflow(workflow=exported_workflow.model_dump_to_import())

    def delete_workflow(self, workflow: str | Workflow2021_1) -> str:
        """
        Delete a workflow from the Itential platform.

        Args:
            workflow (str | Workflow2021_1): The name of the workflow to delete or the Workflow object to delete.

        Returns:
            str: The name of the deleted workflow.
        """
        if isinstance(workflow, Workflow2021_1):
            workflow_name = workflow.name
        elif isinstance(workflow, str):
            workflow_name = workflow
        else:
            raise ValueError(f"Invalid workflow object type: '{type(workflow)}' Requires: 'str' or 'Workflow2021_1'")

        log.debug(f"Existing workflow '{workflow_name}'deleted.")
        response = self.call(method="DELETE", endpoint=f"/workflow_builder/workflows/delete/{workflow_name}")
        if response.ok:
            return response.json()["name"]
        else:
            raise ApiError(response.status_code, f"Api Error: {response.reason} - {response.content}", response.json())
