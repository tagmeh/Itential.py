# Itential.py
A library to (hopefully) make Itential scripting via Python a little easier.

Pypi: https://pypi.org/project/itential.py/

## Remote Install
```text
pip install itential.py
```

## Usage
```python
from itential import Itential
from itential.modules.v2020_2 import AppWorkflowEngine

client = Itential()  # Contains default login and localhost url information

workflow_engine = AppWorkflowEngine(client=client)  # Pass in the auth client

response: "requests.Response" = workflow_engine.get_job_output(job_id="example-job-id")
```

## Local Install
Curently the repository is setup for pipenv. I'm looking into making the repository agnostic to the python environment manager (poetry, pipnev, venv).
```text
pip install pipenv
pipenv install . --dev
```