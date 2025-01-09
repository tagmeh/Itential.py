from src.v2021_1.models.job_model import JobModel2021_1
from src.v2021_1.models.workflow_model import WorkflowModel2021_1

JobModel2021_1.model_rebuild()
WorkflowModel2021_1.model_rebuild()

__all__ = ["JobModel2021_1", "WorkflowModel2021_1"]
