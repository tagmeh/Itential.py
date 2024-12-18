from typing import Type

from itential2.src.versions import SupportedVersion
from itential2.src.asset_classes import asset_versions
from itential2.src.exceptions import NotSupportedError


def get_job_class(version: SupportedVersion) -> Type[asset_versions.Job]:
    match version:
        case SupportedVersion.V2021_1:
            return asset_versions.Job2021_1
        case SupportedVersion.V2023_1:
            return asset_versions.Job2023_1
        case _:
            raise NotSupportedError(f'Jobs for version {version.value} not supported')


def get_workflow_class(version: SupportedVersion, variant: str | None = None) -> Type[asset_versions.Workflow]:
    match version:
        case SupportedVersion.V2021_1:
            if variant == 'export':
                return asset_versions.ExportedWorkflow2021_1
            return asset_versions.Workflow2021_1
        case SupportedVersion.V2023_1:

            raise NotImplementedError(f'Workflows for version {version.value} not yet implemented')
        case _:
            raise NotSupportedError(f'Workflows for version {version.value} not supported')


# def get_catalog_class(version: SupportedVersion) -> Type[asset_versions.Catalog]:
#     match version:
#         case SupportedVersion.V2021_1:
#             return asset_versions.Catalog2021_1
#         case SupportedVersion.V2023_1:
#             raise NotImplementedError(f'Catalogs for version {version.value} not yet implemented')
#         case _:
#             raise NotSupportedError(f'Catalogs for version {version.value} not supported')
