# import warnings
# from functools import wraps
# from typing import Callable, Any
#
# from itential.src.exceptions import NotSupportedError
# from itential.src.iap_versions import v2021_1, v2023_1
# from itential.src.iap_versions.base.models import Workflow, Job
# from itential.src.versions import ItentialVersion
#
#
# def inject_itential_instance(func: Callable) -> Callable:
#     """
#     Injects the 'itential' instance into the returned asset object.
#     This allows the asset instance to make further calls to the Itential instance.
#     """
#
#     @wraps(func)
#     def wrapper(itential, *args, **kwargs):
#         result = func(itential, *args, **kwargs)
#
#         # This is probably an error.
#         # Todo: This section will need updating when the standard error handler is created.
#         if isinstance(result, (str, dict)):
#             return result
#
#         if isinstance(result, list):
#             for item in result:
#                 item._itential = itential
#         else:
#             result._itential = itential
#
#         return result
#
#     return wrapper
#
#
# @inject_itential_instance
# def get_job(itential, job_id: str) -> Job:
#     """
#     Selects the correct version of the get_job function based on the Itential version.
#     """
#     match itential.version:
#         case ItentialVersion.V2021_1:
#             return v2021_1.get_job(itential, job_id)
#         case ItentialVersion.V2023_1:
#             return v2023_1.get_job(itential, job_id)
#         case _:
#             raise NotSupportedError(f'Version {itential.version.value} not supported')
#
#
# @inject_itential_instance
# def get_lean_job(itential, job_id: str, includes: list[str], excludes: list[str], **kwargs) -> Job:
#     """
#     Selects the correct version of the get_lean_job function based on the Itential version.
#     """
#     match itential.version:
#         case ItentialVersion.V2021_1:
#             return v2021_1.get_lean_job(itential, job_id, includes, excludes, **kwargs)
#         case ItentialVersion.V2023_1:
#             return v2023_1.get_lean_job(itential, job_id, includes, excludes, **kwargs)
#         case _:
#             raise NotSupportedError(f'Version {itential.version.value} not supported')
#
#
# @inject_itential_instance
# def get_jobs(itential, workflow_name: str, **kwargs: dict[str, Any]) -> list[Job]:
#     """
#     Selects the correct version of the get_jobs function based on the Itential version.
#     """
#     # Todo: Add a "max_jobs" parameter to limit the number of jobs returned.
#     #  Allows a middle ground between all_jobs and the 1-call limit (100).
#     match itential.version:
#         case ItentialVersion.V2021_1:
#             return v2021_1.get_jobs(itential, workflow_name, **kwargs)
#         case ItentialVersion.V2023_1:
#             return v2023_1.get_jobs(itential, workflow_name, **kwargs)
#         case _:
#             raise NotSupportedError(f'Version {itential.version.value} not supported')
#
#
# @inject_itential_instance
# def get_lean_jobs(itential, job_id: str, includes: list[str], excludes: list[str], **kwargs) -> list[Job]:
#     """
#     Selects the correct version of the get_lean_job function based on the Itential version.
#     """
#     match itential.version:
#         case ItentialVersion.V2021_1:
#             return v2021_1.get_lean_jobs(itential, job_id, includes, excludes, **kwargs)
#         case ItentialVersion.V2023_1:
#             return v2023_1.get_lean_jobs(itential, job_id, includes, excludes, **kwargs)
#         case _:
#             raise NotSupportedError(f'Version {itential.version.value} not supported')
#
#
# @inject_itential_instance
# def get_job_output(itential, job_id: str) -> dict:
#     """
#     Selects the correct version of the get_job_output function based on the Itential version.
#     """
#     match itential.version:
#         case ItentialVersion.V2021_1:
#             return v2021_1.get_job_output(itential, job_id)
#         case ItentialVersion.V2023_1:
#             warnings.warn(
#                 "get_job_output is not needed for version 2023.1 and beyond. This data is returned with the get_job call.",
#                 DeprecationWarning,
#             )
#             return v2023_1.get_job(itential, job_id)
#         case _:
#             raise NotSupportedError(f'Version {itential.version.value} not supported')
#
#
# @inject_itential_instance
# def get_workflow(itential, workflow_name: str) -> Workflow:
#     """
#     Selects the correct version of the get_workflow function based on the Itential version.
#     """
#     match itential.version:
#         case ItentialVersion.V2021_1:
#             return v2021_1.get_workflow(itential, workflow_name)
#         case ItentialVersion.V2023_1:
#             return v2023_1.get_workflow(itential, workflow_name)
#         case _:
#             raise NotSupportedError(f'Version {itential.version.value} not supported')
#
#
# @inject_itential_instance
# def export_workflow(itential, workflow_name: str) -> Workflow:
#     """
#     Selects the correct version of the export_workflow function based on the Itential version.
#     """
#     match itential.version:
#         case ItentialVersion.V2021_1:
#             return v2021_1.export_workflow(itential, workflow_name)
#         case ItentialVersion.V2023_1:
#             return v2023_1.export_workflow(itential, workflow_name)
#         case _:
#             raise NotSupportedError(f'Version {itential.version.value} not supported')
