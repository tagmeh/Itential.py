"""
A "model" within Itential.py is a pydantic model class that represents a data structure from the Itential platform.

Each asset model class inherits the instance of the Itential class instance that created it. This allows the asset
model to interact with the Itential platform directly.
    IE A job model instance could query and return a Workflow model instance via it's .retrieve_workflow() method.

These models are meant to be the return objects when querying the Itential platform.
IE:
    ```
    itential2021_1 = Itential(version=ItentialVersion.2021_1)

    job = itential2021_1.job.retrieve(job_id="1234")
    print(type(job))  # <class 'src.v2021.models.job.JobModel2021_1'>

    workflow = job.retrieve_workflow()
    print(type(job))  # <class 'src.v2021.models.workflow.WorkflowModel2021_1'>
    ```
"""
