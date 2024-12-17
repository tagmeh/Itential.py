from typing import Type

from itential2.src.versions import SupportedVersion
from itential2.src.asset_classes import job_versions
from itential2.src.exceptions import NotSupportedError


def get_job_class(version: SupportedVersion) -> Type[job_versions.Job]:
    match version:
        case SupportedVersion.V2021_1:
            return job_versions.Jobv2021_1
        case SupportedVersion.V2023_1:
            raise NotImplementedError(f'Version {version.value} not yet implemented')
        case _:
            raise NotSupportedError(f'Version {version.value} not supported')

