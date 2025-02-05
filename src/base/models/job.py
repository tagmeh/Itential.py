import logging

from src.base.models.custom_base import CustomBaseModel

log = logging.getLogger(__name__)


class JobModel(CustomBaseModel):
    """
    Pydantic model to represent the Job object.
    """

    # def retrieve_workflow(self) -> "WorkflowResponse":
    #     """Returns the workflow object associated with this job"""
    #     workflow = self.itential_instance.workflow.retrieve(workflow_name=self.name)
    #     return workflow

    def update(self) -> None:
        """
        Updates the job object with the latest information from the Itential instance.
        Also attempts to pull in the job output if the job is complete.
        """
        if self.status in ["complete", "canceled", "error"]:
            print(f"Job '{self.id}' is in a final state ({self.status}) and cannot be updated.")
            return

        job = self.itential_instance.job.retrieve(job_id=self.id)
        self.__dict__.update(job.__dict__)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.id})"
