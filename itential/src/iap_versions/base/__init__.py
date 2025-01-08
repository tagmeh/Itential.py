from itential.src.iap_versions.base.models.catalog import Catalog
from itential.src.iap_versions.base.models.job import Job
from itential.src.iap_versions.base.models.jsonform import JsonForm
from itential.src.iap_versions.base.models.template import Template
from itential.src.iap_versions.base.models.transformation import Transformation
from itential.src.iap_versions.base.models.workflow import Workflow

# Catalog.model_rebuild()
Job.model_rebuild()
# JsonForm.model_rebuild()
# Template.model_rebuild()
# Transformation.model_rebuild()
Workflow.model_rebuild()


__all__ = ["Catalog", "Job", "JsonForm", "Template", "Transformation", "Workflow"]
