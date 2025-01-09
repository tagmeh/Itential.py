"""
An "Asset" within Itential.py is class named after a specific asset within Itential (workflow, catalog, etc.) which
contains the methods used to interact with it. These asset classes are collected within the Itential class instance
such that they are accessed through their respective attribute. This is an organizational choice to keep the Itential
class instance lean and structured.

While a "job" isn't strictly an asset as defined within Itential, it's treated as such for the sake of consistency.
"scripts" is also treated as an asset for consistency reasons, but is not a concept on the Itential Platform.

IE:
    ```
    itential2021_1 = Itential(version=ItentialVersion.2021_1)
    job = itential2021_1.job.retrieve(job_id="1234")
    workflow = itential2021_1.workflow.retrieve(workflow_name=job.name)
    ```
"""
