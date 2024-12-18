from itential2.src.asset_classes.asset_versions import Job, Workflow
from itential2.src.asset_classes.asset_version_factory import get_job_class, get_workflow_class


def get_job(itential, job_id: str) -> Job:
    """
    Get a job by job ID.
    The main difference between this endpoint and get_entire_job is that this endpoint seems to have more concise
    input layouts. Showing just the input json as it was passed in, instead of the input json as it is in the schema
    (more of an exploded schema view). About 20% more concise than get_entire_job (limited testing, ~2350 lines from
    get_entire_job down to ~1875 lines from get_job).

    :param job_id: Returned when creating a job or querying for jobs by workflow name.
        Ex: "ec59ef85fef84e59bf36bd1e"
    :return: requests.Response
    """
    response = itential.call(method="GET", endpoint=f"/workflow_engine/getJob/{job_id}")
    if response.ok:
        return get_job_class(version=itential.version)(**response.json())
    else:
        return response.reason  # Todo: Add error handling


def get_workflow(itential, workflow_name: str) -> Workflow:
    """
    Uses a static payload with the workflow_engine/workflows/search endpoint.
    The main difference between this function and export_workflow is that get_workflow has an "_id" and "errors"
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
            return get_workflow_class(version=itential.version)(**response.json()['results'][0])
    else:
        return response.reason


def export_workflow(itential, workflow_name: str) -> Workflow:
    """Export a single workflow."""
    payload = {"options": {"name": workflow_name, "type": "automation"}}
    response = itential.call(method="POST", endpoint='/workflow_builder/export', json=payload)
    if response.ok:
        return get_workflow_class(version=itential.version, variant='export')(**response.json())
    else:
        return response.reason
