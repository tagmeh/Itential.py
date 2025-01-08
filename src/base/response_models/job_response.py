from typing import Optional

from pydantic import BaseModel


class Job(BaseModel):
    """
    Pydantic model to represent the Job object.
    Includes related methods to act upon the job object via the itential instance.

    model.dict() - Same as model.model_dump(model='python')
    model.model_dump(mode='json') - Outputs the object with resolved fields (like datetime > string)
    model.model_dump(mode='python') - Outputs the object with unresolved fields (like datetime > datetime object)
    model.model_dump_json() - Outputs a json string representation of the object. (string, nulls, true/false, "quotes")
    """
    itential_instance: Optional["Itential"] = None
    name: str | None  # Name of the Job's workflow
    id: str | None  # ID of the job instance

    def retrieve_workflow(self):
        """Returns the workflow object associated with this job"""
        workflow = self.itential_instance.workflow.retrieve(workflow_name=self.name)
        return workflow

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
