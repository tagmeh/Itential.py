# Itential.py
#### An effort to write a python library for the Itential API. (https://apidocs.itential.com/api/)

Usage
```python
from itential import Itential
from itential.modules.v2020_2 import AppWorkflowEngine

client = Itential()  # Contains default login and localhost url information

response: "requests.Response" = AppWorkflowEngine.get_job_output(client=client, job_id="example-job-id")
```