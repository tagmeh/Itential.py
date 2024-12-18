from itential2.src.asset_classes.asset_versions import Job, Workflow
from itential2.src.versions import SupportedVersion
from itential2.src.exceptions import NotSupportedError

from itential2.src.endpoints.endpoint_versions import v2021_1, v2023_1


def get_job(itential, job_id: str) -> Job:
    match itential.version:
        case SupportedVersion.V2021_1:
            return v2021_1.get_job(itential, job_id)
        case SupportedVersion.V2023_1:
            return v2023_1.get_job(itential, job_id)
        case _:
            raise NotSupportedError(f'Version {itential.version.value} not supported')


def get_workflow(itential, workflow_name: str) -> Workflow:
    match itential.version:
        case SupportedVersion.V2021_1:
            return v2021_1.get_workflow(itential, workflow_name)
        case SupportedVersion.V2023_1:
            raise NotImplementedError(
                f'get_workflow is not implemented in {SupportedVersion.V2023_1.value}. Use export_workflow instead.'
            )
        case _:
            raise NotSupportedError(f'Version {itential.version.value} not supported')


def export_workflow(itential, workflow_name: str) -> Workflow:
    match itential.version:
        case SupportedVersion.V2021_1:
            return v2021_1.export_workflow(itential, workflow_name)
        case SupportedVersion.V2023_1:
            return v2023_1.export_workflow(itential, workflow_name)
        case _:
            raise NotSupportedError(f'Version {itential.version.value} not supported')