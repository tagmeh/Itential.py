from typing import Type, TYPE_CHECKING, Any, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from itential import Itential


class Job(BaseModel):
    _itential: Optional["Itential"] = None  # Itential state instance.
    name: str | None  # Name of the Job's workflow
    id: str | None  # ID of the job instance

    def get_workflow(self) -> "Workflow":
        """Returns the workflow object associated with this job"""
        #  Lazy loading to avoid circular dependencies on load. Unsure if this is a bad idea atm.

        workflow: "Workflow" = self._itential.get_workflow(workflow_name=self.name)
        return workflow

    def export_workflow(self) -> "Workflow":
        """Returns the workflow object associated with this job"""

        workflow: "Workflow" = self._itential.export_workflow(workflow_name=self.name)
        return workflow

    def update(self) -> None:
        """
        Updates the job object with the latest information from the Itential instance.
        Also attempts to pull in the job output if the job is complete.
        """
        if self.status in ["complete", "canceled", "error"]:
            print(f"Job '{self.id}' is in a final state ({self.status}) and cannot be updated.")
            return

        job = self._itential.get_job(job_id=self.id)
        self.__dict__.update(job.__dict__)

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

    def get_jobs(self, get_all: bool = False, limit: int = 10, **kwargs: Any) -> list[Job]:
        """Returns a list of jobs associated with this workflow"""
        jobs: list[Job] = self._itential.get_jobs(workflow_name=self.name, get_all=get_all, limit=limit, **kwargs)
        return jobs

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name})"


class Catalog(BaseModel):
    _itential: Optional["Itential"] = None
    pass
