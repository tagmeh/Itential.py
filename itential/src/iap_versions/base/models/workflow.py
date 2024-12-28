from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from itential import Itential
    from itential.src.iap_versions.base import Job


class Workflow(BaseModel):
    _itential: Optional["Itential"] = None  # Itential state instance.
    name: str | None  # Name of the workflow, unique to the IAP platform.

    def get_jobs(self, get_all: bool = False, limit: int = 10, **kwargs: Any) -> list["Job"]:
        """Returns a list of jobs associated with this workflow"""
        jobs: list[Job] = self._itential.get_jobs(workflow_name=self.name, get_all=get_all, limit=limit, **kwargs)
        return jobs

    @abstractmethod
    def model_dump_to_import(self):
        """
        Outputs a cleaned up json object that can be imported into the Itential platform.

        Returns:
            dict: The cleaned up json object.
        """
        ...

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name})"
