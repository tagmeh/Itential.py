# Itential.py
#### An effort to write a python library for the Itential API. (https://apidocs.itential.com/2021.2/api/) (New Link to Old Docs)

8.5.2022 - I took a break after Itential updated their documentation, and broke all of their existing links (including every link I had posted in the method doc strings...). Pretty demoralizing, and a month or so after the Great Link Breakin'ing, they are still all broken. But, my motivation has returned, and work will continue. I plan on getting this pushed out as a package as quickly as possible.

Usage
```python
from itential import Itential
from itential.modules.v2020_2 import AppWorkflowEngine

client = Itential()  # Contains default login and localhost url information

response: "requests.Response" = AppWorkflowEngine.get_job_output(client=client, job_id="example-job-id")
```
