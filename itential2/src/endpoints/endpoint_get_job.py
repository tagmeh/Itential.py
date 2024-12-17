from typing import overload

from itential2.src.asset_classes.job_versions import Job
from itential2.src.versions import SupportedVersion
from itential2.src.exceptions import NotSupportedError
from itential2.src.asset_classes.job import get_job_class


# Show type hinting for get_job as just "job_id: str", the "itential" parameter is injected by the Itential class
# @overload
# def get_job(job_id: str) -> Job:
#     ...


def get_job(itential, job_id: str) -> Job:
    
    match itential.version:
        case SupportedVersion.V2021_1:
            return get_job_v2021_1(itential, job_id)
        case SupportedVersion.V2023_1:
            raise NotImplementedError(f'Version {itential.version.value} not yet implemented')
        case _:
            raise NotSupportedError(f'Version {itential.version.value} not supported')


def get_job_v2021_1(itential, job_id: str) -> Job:
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
        job_class = get_job_class(version=itential.version)
        return job_class(**response.json())
    else:
        return response  # Todo: Add error handling