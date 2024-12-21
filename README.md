# Itential.py
## An opinionated Python interface for the Itential API.

**This project is not affiliated with Itential in any way.**

### Introduction
The goal of this project is a few-fold:
1. To make writing scripts around the Itential API easier.
2. As a fun project to learn more about Python.

Hopefully, others will find it useful as well. Assuming there isn't already some corporate-sponsored mega-library out there with all the bells and whistles already.

I personally only plan on supporting the versions of Itential I have access to and use regularly.
I don't plan on implementing every endpoint or feature of every Itential version.

Itential versions are separated by the Year.Major (2021.1, 2022.2, etc.). As of this writing, 
the minors are not considered (2021.1.1). That may change in the future, as we have had breaking changes 
come about in a minor release before. Though, the expectation is that it shouldn't happen going forward.

I'm open to contributions, just bare with me, I don't have the fancy infrastructure in place for everything yet. 

***Constructive*** feedback is always appreciated.

### Features
- Standardizes dates into datetime objects (Itential returns a mix of timestamps and ISO formats)
- Standardizes asset property formats (Itential returns a mix of camelCase and snake_case)
- Converts assets and jobs into Pydantic models for type hinting and validation
- Authentication and token management is handled by the Itential instance. 
  - You can create multiple instances for different Itential versions at the same time (1 instance per version of course. There's no enforced limit except that the Itential token will change on each authentication, invalidating the previous instances of the same version.).
- Pydantic models allow access to certain methods. 
  - Examples:
    - A job object has a method to query it's associated workflow, returning a workflow object.
      - Job.get_workflow()
    - A workflow object can be used to get n number of associated jobs.
      - Workflow.get_jobs(limit=50)

### Scope
**Currently, the only supported versions of Itential are 2021.1.x and 2023.1.x.**

Going forward, we'll support what's available, as we can. 
As mentioned above, the goal isn't complete coverage of Itential's API and features, but the most useful and most used endpoints to make our lives easier.

We use Pydantic models for Job/Workflow/Etc objects, per Itential version and Requests for the HTTP requests. 

We try to document the Itential endpoints with at least the information given by Itential, though, it often needs improvement, or edge/use cases need defining.

### Installation
```bash
pip install itential.py
```

### Usage
Type-hinting is still a work in progress.

The idea is to have an Itential instance that authenticates with a given server and from which you can get jobs, workflows, other assets.
If you have access to multiple Itential platform versions, you can create and authenticate multiple Itential instances.

Local Itential Instance Example
```python
from itential import Itential, ItentialVersion

# Login to a local Itential with default auth and url.
iap_2021_1 = Itential(version=ItentialVersion.V2021_1)

# Get a job by ID using the Itential instance.
single_job = iap_2021_1.get_job(job_id="3a27928f699e4658b4df5aeb")
print(single_job.name)  # "Cool Workflow"
# print(type(single_job))  # <class 'Job2021_1'>  subclassed from <class 'Job'>

# Get the workflow associated with the job.
cool_workflow = single_job.get_workflow()
print(cool_workflow.name)  # "Cool Workflow"
# print(type(cool_workflow))  # <class 'Workflow2021_1'> subclassed from <class 'Workflow'> 

# Get a workflow by name using the Itential instance.
another_workflow = iap_2021_1.get_workflow(workflow_name="Another Workflow")
print(another_workflow.name)  # "Another Workflow"
# print(type(another_workflow))  # <class 'Workflow2021_1'>

# Get the jobs associated with the workflow.
cool_workflow_jobs = cool_workflow.get_jobs(limit=50)
print(len(cool_workflow_jobs))  # 50
# print(type(cool_workflow_jobs[0]))  # list[<class 'Job2021_1'>] 
```

Remote Itential Instance Example
```python
from itential import Itential, ItentialVersion

# Login to a remote Itential with custom auth and url.
iap_2023_1 = Itential(
    version=ItentialVersion.V2023_1,
    url="https://my.itential.com",
    username="my_username",
    password="my_password"
)

# Get a job by ID using the Itential instance.
single_job = iap_2023_1.get_job(job_id="3a27928f699e4658b4df5aeb")
```

### Potential/Planned Features/Goals
- [ ] Easier export/import of repository assets (workflows, JSTs, catalogs, etc.)
- [ ] Easier Job querying and parsing.
- [ ] Conversion tools from one version to another? (2021.1 workflow into a 2023.1 workflow)
- [ ] Validation tools for an app/adapter's repo in the local, or a remote instance?
- [ ] Custom objects for handling lists of jobs (not unlike Django's QuerySet maybe)?
- [ ] Making friends along the way.