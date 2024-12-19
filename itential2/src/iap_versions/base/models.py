from typing import Type, TYPE_CHECKING, Any, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from itential2 import Itential


class Job(BaseModel):
    _itential: Optional["Itential"] = None  # Itential state instance.
    name: str | None  # Name of the Job's workflow
    id: str | None  # ID of the job instance

    def get_workflow(self) -> "Workflow":
        """Returns the workflow object associated with this job"""
        #  Lazy loading to avoid circular dependencies on load. Unsure if this is a bad idea atm.
        from itential2.src.iap_versions.endpoint_version_factory import get_workflow

        workflow: "Workflow" = get_workflow(self._itential, self.name)  # Explicitly for mypy typing.
        return workflow

    def export_workflow(self) -> "Workflow":
        """Returns the workflow object associated with this job"""
        from itential2.src.iap_versions.endpoint_version_factory import export_workflow

        workflow: "Workflow" = export_workflow(self._itential, self.name)  # Explicitly for mypy typing.
        return workflow

    # Todo: Would be nice to have the __repr__ return something like <Job2023_1 (id)> or something better than
    #  the full path to this class when printing type(job)
    #
    # def __repr__(self):
    #     return f"{self.__name__} ({self.id})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.id})"


class Workflow(BaseModel):
    _itential: Optional["Itential"] = None  # Itential state instance.
    name: str | None  # Name of the workflow, unique to the IAP platform.

    def get_jobs(self, all_jobs: bool = False, limit: int = 10, **kwargs: Any) -> list[Job]:
        """Returns a list of jobs associated with this workflow"""
        from itential2.src.iap_versions.endpoint_version_factory import get_jobs

        jobs: list[Job] = get_jobs(  # Explicitly for mypy typing.
            itential=self._itential,
            workflow_name=self.name,
            all_jobs=all_jobs,
            limit=limit, **kwargs
        )
        return jobs

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name})"


class Catalog(BaseModel):
    _itential: Optional["Itential"] = None
    pass
