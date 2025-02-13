import logging
from abc import abstractmethod

from src.base.models.custom_base import CustomBaseModel

log = logging.getLogger(__name__)


class WorkflowModel(CustomBaseModel):
    """
    Represents a workflow in the Itential Automation Platform (IAP).
    """

    name: str | None  # Name of the workflow, unique to the IAP platform.

    # def get_jobs(self, get_all: bool = False, limit: int = 10, **kwargs: Any) -> list:
    #     """Returns a list of jobs associated with this workflow"""
    #     jobs = self.itential_instance.job.search(workflow_name=self.name, get_all=get_all, limit=limit, **kwargs)
    #     return jobs

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
