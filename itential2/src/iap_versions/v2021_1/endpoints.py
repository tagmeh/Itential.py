import logging

from itential.src.iap_versions.v2021_1 import models

log = logging.getLogger(__name__)


def get_job(itential, job_id: str) -> models.Job2021_1:
    """
    Get a job by job ID.
    The main difference between this endpoint and get_entire_job is that this endpoint seems to have more concise
    input layouts. Showing just the input json as it was passed in, instead of the input json as it is in the schema
    (more of an exploded schema view). About 20% more concise than get_entire_job (limited testing, ~2350 lines from
    get_entire_job down to ~1875 lines from get_job).

    :param itential: Itential state object, holds the authentication and makes the api calls.
    :param job_id: Returned when creating a job or querying for jobs by workflow name.
        Ex: "ec59ef85fef84e59bf36bd1e"
    """
    response = itential.call(method="GET", endpoint=f"/workflow_engine/getJob/{job_id}")
    if response.ok:
        return models.Job2021_1(**response.json())
    else:
        return response.reason  # Todo: Add error handling or error class object


def get_lean_job(itential, job_id: str, includes: list[str], excludes: list[str], **kwargs) -> models.Job2021_1 | None:
    """
    Returns a Job object with only the specified fields filled in. A hard-coded query should limit the number of jobs
    found to between 0 and 1.

    Args:
        itential (Itential): The Itential state object
        job_id (str): The job_id to retrieve
        includes (list[str]): The fields to include in the job object. Exclusive with excludes.
        excludes (list[str]): The fields to exclude in the job object. Exclusive with includes.
        **kwargs (dict): Additional arguments for the workflow_engine/jobs/search endpoint. See get_jobs() for more info.

    Returns (Job): A Job object with only the specified fields filled in.
    """
    if includes:
        filter_dict = {prop: 1 for prop in includes}
    elif excludes:
        filter_dict = {prop: 0 for prop in excludes}
    else:
        raise ValueError("Either includes or excludes must be provided.")

    jobs: list[models.Job2021_1] = get_jobs(itential, query={"_id": job_id}, limit=1, fields=filter_dict, **kwargs)

    if len(jobs) == 1:
        return jobs[0]
    if len(jobs) == 0:
        log.error(f"No job found with id: {job_id}")
        return None


def get_jobs(
    itential,
    workflow_name: str | None = None,
    all_jobs: bool = False,
    max_jobs: int | None = None,
    limit: int = 10,
    skip: int = 0,
    sort: dict[str, int] = None,
    fields: dict[str, int] = None,
    **kwargs,
) -> list[models.Job2021_1] | list:
    """
    Get all jobs for a workflow.
    Search jobs with Options. This is similar to search_workflows, but with some additional fields.

    Args:
        itential: The Itential state object
        workflow_name: The name of the workflow to search for. Opinionated and optional.
        all_jobs: If True, will return all jobs for the workflow. If False, will return the first page of jobs.
        max_jobs:
        limit: Max results to return
        skip: Number to offset the search by
        sort: {"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
        fields: {"name": 1}. "name" field can be any field in the workflow json. Used to filter out other fields

    Keyword Args:
        expand: {"expand": ["user"]}. Instructs the API to return the full object for the specified field.
        query: {"name": "workflow_name"}. "name" field can be any field in the workflow json.
        local:

    Examples:
        get_jobs(itential, workflow_name="abcd", limit=50, sort={"name": -1})

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

    # Default query parameters.
    payload = {
        "options": {
            "limit": limit,
            "skip": skip,
            "sort": {"metrics.start_time": -1},
            **kwargs,
        }
    }

    if sort:  # Override the default sort if a sort is passed in.
        payload["options"]["sort"] = sort

    if fields:
        payload["options"]["fields"] = fields
    else:
        # Exclude large fields by default.
        payload["options"]["fields"] = {"tasks": 0, "transitions": 0}

    if workflow_name:
        # If workflow_name, then do a simple "equals" query against the workflow_name.
        payload.update(**{"query": {"name": workflow_name}})

    log.debug(f"'get_jobs' payload: {payload}")

    response = itential.call(method="POST", endpoint=f"/workflow_engine/jobs/search", json=payload)
    if response.ok:
        response_json = response.json()

        if all_jobs is True:
            jobs: list[dict] = response_json['results']

            while response_json['metadata']['nextPageSkip'] is not None:
                if max_jobs and len(jobs) >= max_jobs:
                    break

                payload["skip"] = response_json['metadata']['nextPageSkip']

                response = itential.call(method="POST", endpoint=f"/workflow_engine/jobs/search", json=payload)
                response_json = response.json()
                jobs.extend(response_json['results'])

        else:
            jobs = response_json['results']

        if max_jobs:
            jobs = jobs[:max_jobs]

        return [models.Job2021_1(**job) for job in jobs]
    else:
        return response.reason  # Todo Output standardized error object.


def get_job_output(itential, job_id: str) -> models.Job2021_1:
    """Gets the output of the Job if the job is completed (but not cancelled)"""
    response = itential.call(method="GET", endpoint=f"/workflow_engine/job/{job_id}/output")
    if response.ok:
        return models.Job2021_1(id=job_id, variables=response.json())
    else:
        return response.reason


def get_workflow(itential, workflow_name: str) -> models.Workflow2021_1:
    """
    Uses a static payload with the workflow_engine/workflows/search endpoint.
    The main difference between this function and export_workflow is that get_workflow has an "id" and "errors"
      key in the response json, while export_workflow does not. export_workflow also has the user objects expanded by
      default, but the get_workflow has to pass in the "expand" option (as seen below).
    """
    payload = {"options": {"expand": ["last_updated_by", "created_by"], "query": {"name": workflow_name}}}
    response = itential.call(method="POST", endpoint='/workflow_engine/workflows/search', json=payload)
    if response.ok:
        response_json = response.json()
        if response_json['total'] == 0:
            raise ValueError(f'No workflows found with name: {workflow_name}')
        elif response_json['total'] > 1:
            raise ValueError(f'Multiple workflows found with name: {workflow_name}')
        elif response_json['total'] == 1:
            return models.Workflow2021_1(**response.json()['results'][0])
    else:
        return response.reason


def export_workflow(itential, workflow_name: str) -> models.ExportedWorkflow2021_1:
    """Export a single workflow."""
    payload = {"options": {"name": workflow_name, "type": "automation"}}
    response = itential.call(method="POST", endpoint='/workflow_builder/export', json=payload)
    if response.ok:
        return models.ExportedWorkflow2021_1(**response.json())
    else:
        return response.reason
