"""
Link to Itential Docs: https://apidocs.itential.com/2020.2/api/app-workflow_engine/

Implemented  Doc String  Tests  Fix Method Tooltip
    [x]         [x]       [ ]         [ ]   activate
    [-]         [-]       [-]         [ ]   addDuration
    [x]         [x]       [ ]         [ ]   addWatchers
    [-]         [-]       [-]         [ ]   arrayConcat
    [-]         [-]       [-]         [ ]   arrayIncludes
    [-]         [-]       [-]         [ ]   arrayIndexOf
    [-]         [-]       [-]         [ ]   arrayLastIndexOf
    [-]         [-]       [-]         [ ]   arrayLength
    [-]         [-]       [-]         [ ]   arrayPop
    [-]         [-]       [-]         [ ]   arrayPush
    [-]         [-]       [-]         [ ]   arrayShift
    [-]         [-]       [-]         [ ]   arraySlice
    [-]         [-]       [-]         [ ]   arrayToLocaleString
    [-]         [-]       [-]         [ ]   arrayToString
    [-]         [-]       [-]         [ ]   assign
    [-]         [-]       [-]         [ ]   calculateTimeDiff
    [x]         [x]       [ ]         [ ]   cancelJob
    [-]         [-]       [-]         [ ]   charAt
    [-]         [-]       [-]         [ ]   charCodeAt
    [x]         [x]       [ ]         [ ]   checkWorkflowForJobVariables
    [-]         [-]       [-]         [ ]   childJob
    [x]         [x]       [-]         [ ]   claimTask
    [-]         [-]       [-]         [ ]   codePointAt
    [-]         [-]       [-]         [ ]   convertEpochToObject
    [-]         [-]       [-]         [ ]   convertTimeFormat
    [-]         [-]       [-]         [ ]   convertTimeToEpoch
    [-]         [-]       [-]         [ ]   convertTimezone
    [-]         [-]       [-]         [ ]   copyWithin
    [x]         [x]       [ ]         [ ]   createJobGroupEntry
    [x]         [x]       [ ]         [ ]   deactivate
    [-]         [-]       [-]         [ ]   decision
    [-]         [-]       [-]         [ ]   deepmerge
    [-]         [-]       [-]         [ ]   delay
    [x]         [x]       [ ]         [ ]   deleteJobGroups
    [x]         [x]       [ ]         [ ]   diffToHTML
    [-]         [-]       [-]         [ ]   endsWith
    [-]         [-]       [-]         [ ]   ErrorHandling
    [-]         [-]       [-]         [ ]   evaluation
    [-]         [-]       [-]         [ ]   eventListenerJob
    [-]         [-]       [-]         [ ]   extractField
    [-]         [-]       [-]         [ ]   fill
    [x]         [x]       [ ]         [ ]   find
    [x]         [x]       [ ]         [ ]   findForwardPaths
    [x]         [x]       [ ]         [ ]   finishManualTask
    [x]         [x]       [ ]         [ ]   fixJob
    [-]         [-]       [-]         [-]   FlattenJSONFormInput
    [-]         [-]       [-]         [-]   forEach
    [-]         [-]       [-]         [-]   getAllLoopTasks
    [x]         [x]       [ ]         [x]   getAssociatedJobs
    [x]         [x]       [ ]         [x]   getEntireJob
    [x]         [x]       [ ]         [x]   getJob
    [x]         [x]       [ ]         [x]   getJobDetails
    [x]         [x]       [ ]         [x]   getJobFromTaskQuery
    [x]         [x]       [ ]         [x]   getJobList
    [x]         [x]       [ ]         [ ]   getJobOutput
    [x]         [x]       [ ]         [x]   getJobShallow
    [x]         [x]       [ ]         [x]   getJobVisualizationData
    [x]         [x]       [ ]         [x]   getManualTaskController
    [x]         [x]       [ ]         [x]   getTask
    [x]         [x]       [ ]         [x]   getTaskDetails
    [x]         [x]       [ ]         [x]   getTaskStatuses
    [-]         [-]       [-]         [-]   getTime
    [x]         [x]       [ ]         [x]   getWorkflowsDetailedByName
    [x]         [x]       [ ]         [x]   isActive
    [-]         [-]       [-]         [-]   isArray
    [-]         [-]       [-]         [-]   join
    [-]         [-]       [-]         [-]   keys
    [x]         [x]       [ ]         [x]   listJobGroups
    [-]         [-]       [-]         [-]   localeCompare
    [-]         [-]       [-]         [-]   makeData
    [-]         [-]       [-]         [-]   map
    [-]         [-]       [-]         [-]   match
    [-]         [-]       [-]         [-]   merge
    [-]         [-]       [-]         [-]   modify
    [-]         [-]       [-]         [-]   newVariable
    [-]         [-]       [-]         [-]   normalize
    [-]         [-]       [-]         [-]   numberToString
    [-]         [-]       [-]         [-]   objectHasOwnProperty
    [-]         [-]       [-]         [-]   objectToString
    [-]         [-]       [-]         [-]   padEnd
    [-]         [-]       [-]         [-]   padStart
    [-]         [-]       [-]         [-]   parse
    [-]         [-]       [-]         [-]   parseInt
    [x]         [x]       [ ]         [x]   pauseJob
    [-]         [-]       [-]         [-]   pop
    [x]         [x]       [ ]         [x]   prepareMetricsLogs
    [-]         [-]       [-]         [-]   push
    [-]         [-]       [-]         [-]   query
    [x]         [x]       [ ]         [x]   queryJobs
    [x]         [x]       [ ]         [x]   queryTasksBrief
    [x]         [x]       [ ]         [x]   releaseTask
    [x]         [x]       [ ]         [x]   removeJobGroup
    [-]         [-]       [-]         [-]   repeat
    [-]         [-]       [-]         [-]   replace
    [x]         [x]       [ ]         [x]   replaceJobGroups
    [-]         [-]       [-]         [-]   restCall
    [x]         [x]       [ ]         [x]   resumeJob
    [-]         [-]       [-]         [-]   reverse
    [x]         [x]       [ ]         [x]   revertToTask
    [x]         [x]       [ ]         [x]   runEvaluationGroup
    [x]         [x]       [ ]         [x]   runEvaluationGroups
    [x]         [x]       [ ]         [x]   runValidation
    [-]         [-]       [-]         [-]   search
    [x]         [x]       [ ]         [x]   searchJobs
    [x]         [x]       [ ]         [x]   searchTasks
    [x]         [x]       [ ]         [x]   searchWorkflows
    [-]         [-]       [-]         [-]   setObjectKey
    [-]         [-]       [-]         [-]   shift
    [-]         [-]       [-]         [-]   sort
    [-]         [-]       [-]         [-]   split
    [x]         [x]       [ ]         [x]   startJobWithOptions
    [-]         [-]       [-]         [-]   startsWith
    [-]         [-]       [-]         [-]   stringConcat
    [-]         [-]       [-]         [-]   stringIncludes
    [-]         [-]       [-]         [-]   stringIndexOf
    [-]         [-]       [-]         [-]   stringLastIndexOf
    [-]         [-]       [-]         [-]   stringLength
    [-]         [-]       [-]         [-]   stringSlice
    [-]         [-]       [-]         [-]   stringValueOf
    [-]         [-]       [-]         [-]   stub
    [-]         [-]       [-]         [-]   substring
    [-]         [-]       [-]         [-]   toLocaleLowerCase
    [-]         [-]       [-]         [-]   toLocaleUpperCase
    [-]         [-]       [-]         [-]   toLowerCase
    [-]         [-]       [-]         [-]   toUpperCase
    [-]         [-]       [-]         [-]   transformation
    [-]         [-]       [-]         [-]   trim
    [-]         [-]       [-]         [-]   trimEnd
    [-]         [-]       [-]         [-]   trimStart
    [-]         [-]       [-]         [-]   unshift
    [x]         [x]       [ ]         [x]   unwatchJob
    [-]         [-]       [-]         [-]   updateJobDescription
    [x]         [x]       [ ]         [x]   validateAllLoops
    [-]         [-]       [-]         [-]   values
    [-]         [-]       [-]         [-]   ViewData
    [-]         [-]       [-]         [-]   ViewDiff
    [x]         [x]       [ ]         [x]   watchJob
"""
import warnings
from typing import TYPE_CHECKING, Optional, Dict, Any, List

import requests

if TYPE_CHECKING:
    from itential.core import Itential


class AppWorkflowEngine:
    """https://apidocs.itential.com/2020.2/api/app-workflow_engine/"""

    def __init__(self, client: "Itential"):
        self.client = client

    def activate(self, **kwargs: Dict[str, Any]) -> requests.Response:
        """
        Activate Task Worker ( API payload not documented. May not be usable/implemented )
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/activate/
        :param kwargs: Undocumented payload kwargs
        :return: Status flag of activation
        """
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/activate", json=kwargs)

    def add_watchers(self, job_id: str, watchers: List[str]) -> requests.Response:
        """
        Add users to the watchers list of a job by job ID and username.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/addWatchers/

        :param job_id: ID of the job to watch.
        :param watchers: Users to add to watchers list.
        :return: User IDs added to the watchers list.
        """
        body = {"job_id": job_id, "watchers": watchers}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/job/watchers/watch", json=body)

    def cancel_job(self, job_id: str) -> requests.Response:
        """
        Cancel an active job by job ID.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/cancelJob/

        :param job_id: ID of the job to cancel.
        :return: Data from the canceled job.
        """
        body = {"job_id": job_id}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/cancelJob", json=body)

    def check_workflow_for_job_variables(self, workflow_name: str) -> requests.Response:
        """
        Get job variables of a workflow by workflow name.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/checkWorkflowForJobVariables/

        :param workflow_name: Name of the workflow.
        :return: Variables of the workflow matching the name.
        """
        return self.client.call(
            method="GET", url=f"{self.client.url}/workflow_engine/workflows/variables/{workflow_name}"
        )

    def claim_task(self, task_id: str, user: str) -> requests.Response:
        """
        Claim a manual Task
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/claimTask/

        :param task_id: ID of the Task to claim.
        :param user: User id for the user claiming the Task.
        :return: Result of claiming the Task.
        """
        body = {"task_id": task_id, "user": user}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/tasks/claim", json=body)

    def create_job_group_entry(self, job_id: str, group_id: str) -> requests.Response:
        """
        Add a group to the list of groups for a job.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/createJobGroupEntry/

        :param job_id: ID of job
        :param group_id: A Group id
        :return: Status of adding a group to a job.
        """
        body = {"group": group_id}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/jobs/{job_id}/groups", json=body)

    def deactivate(self, **kwargs: Dict[str, Any]) -> requests.Response:
        """
        Deactivate Task Worker ( API payload not documented. May not be usable/implemented )
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/deactivate/

        :param kwargs: Undocumented POST payload
        :return: Status flag of deactivation
        """
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/deactivate", json=kwargs)

    def delete_job_groups(self, job_id: str) -> requests.Response:
        """
        Remove all authorization restriction for a job.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/deleteJobGroups/

        :param job_id: ID of job
        :return: Status of Delete
        """
        return self.client.call(method="DELETE", url=f"{self.client.url}/workflow_engine/jobs/{job_id}/groups")

    def diff_to_html(self, label1: str, value1: str, label2: str, value2: str) -> requests.Response:
        """
        DEPRECIATED: Difference between two values in HTML response
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/diffToHTML/

        :param label1: Optional label for value1
        :param value1: Any value to diff against value2
        :param label2: Optional label for value2
        :param value2: Any value to diff against value1
        :return: HTML difference between value1 and value2
        """
        warnings.warn("Marked as depreciated by Itential.", PendingDeprecationWarning)
        body = {"label1": label1, "value1": value1, "label2": label2, "value2": value2}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/diffToHTML", json=body)

    def find(self, query: Dict[str, Any], options: Dict[str, Any]) -> requests.Response:
        """
        Find job Documents based on a query and additional options.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/find/

        :param query: A MongoDB query object. See docs for an example
        :param options: A MongoDB options object. See docs for an example
        :return: Resulting job Documents that matched query and options.
        """
        body = {"query": query, "options": options}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/jobs/find", json=body)

    def find_forward_paths(
        self, start_task_id: str, end_task_id: str, workflow_details: Dict[str, Any]
    ) -> requests.Response:
        """
        Find the paths between two Tasks in a Workflow by Task ids and Workflow details.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/findForwardPaths/

        :param start_task_id: ID of the start Task.
        :param end_task_id: ID of the end Task.
        :param workflow_details: Workflow data which contain the tasks and transitions properties of the workflow.
        :return: All valid paths between the Tasks.
        """
        body = {"start_task": start_task_id, "end_task": end_task_id, "workflow_details": workflow_details}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/findForwardPaths", json=body)

    def finish_manual_task(self, task_id: str, job_id: str, task_data: Dict[str, Any]) -> requests.Response:
        """
        Finishes a manual task with finish state success
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/finishManualTask/

        :param task_id: ID of the Task within that job.
        :param job_id: ID of the Job.
        :param task_data: Data of the completed Task.
        :return: The Current Job Object
        """
        body = {"task_id": task_id, "job_id": job_id, "task_data": task_data}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/finishTask", json=body)

    def fix_job(self, job_id: str, errored_task: str, revert_task: str) -> requests.Response:
        """
        Revert an errored job to a target task by job ID and task names.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/fixJob/

        :param job_id: ID of the job to fix.
        :param errored_task: Name of the errored Task.
        :param revert_task: Name of the target Task.
        :return: Job after the revert.
        """
        body = {"job_id": job_id, "errored_task": errored_task, "revert_task": revert_task}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/fixJob", json=body)

    def get_all_loop_tasks(self, workflow_details: Dict[str, Any]) -> requests.Response:
        """
        Get all looped Tasks in a Workflow by Workflow details.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getAllLoopTasks/

        :param workflow_details: Workflow to get looped tasks.
        :return: looped Tasks of the Workflow.
        """
        body = {"workflow_details": workflow_details}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/getAllLoopTasks", json=body)

    def start_job_with_options(self, workflow_name: str, options: Dict[str, Any]) -> requests.Response:
        """
        Initiate a job of a workflow with options.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/startJobWithOptions/

        :param workflow_name: Name of the workflow from which to start the job.
        :param options: Parameters to start the workflow with
            Ex: "options": {
                    "description": "str",
                    "variables": {
                        "incoming": {
                        ...
                        }
                    }
                }
        :return: Job which is started.
        """
        body = {"options": options}
        return self.client.call(
            method="POST", url=f"{self.client.url}/workflow_engine/startJobWithOptions/{workflow_name}", json=body
        )

    def get_associated_jobs(
        self,
        filters: Optional[Dict[str, str]] = None,
        sort: Optional[Dict[str, int]] = None,
        limit: int = 10,
        skip: int = 0,
    ) -> requests.Response:
        """
        Search for jobs that the user has touched.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getAssociatedJobs/

        :param filters: Ex: {"metrics.user": "admin@pronghorn"} to filter for a specific user.
        :param skip: Number of jobs to offset the result. Useful for pagination.
        :param sort: {"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
        :param limit: Set to 0 to disable pagination.
        :return: All matching jobs. example json(): {"results": ["_id": int, "name": str],
         "skip": int, "limit": int, "total": int}
        """

        body = {
            "options": {
                # filter: {"key.path": "value"}  Added below
                "page": {"skip": skip, "limit": limit},
                "sort": {"field": "name", "direction": -1},
            }
        }

        if filters:
            body["options"]["filter"] = filters

        if sort:
            body["options"]["sort"] = sort

        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/getAllLoopTasks", json=body)

    def get_entire_job(self, job_id: str) -> requests.Response:
        """
        Get entire data of a job by job ID.
        Returns an "exploded" view, where data input into tasks is displayed in a schema view as opposed to the same
        format as it was originally passed in as. Contained about 20% more lines than get_job without containing any
        additional data.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getEntireJob/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/getEntireJob/{job_id}")

    def get_job(self, job_id: str) -> requests.Response:
        """
        Get a job by job ID.
        The main difference between this endpoint and get_entire_job is that this endpoint seems to have more concise
        input layouts. Showing just the input json as it was passed in, instead of the input json as it is in the schema
        (more of an exploded schema view). About 20% more concise than get_entire_job (limited testing, ~2350 lines from
        get_entire_job down to ~1875 lines from get_job).
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getJob/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/getJob/{job_id}")

    def get_job_details(self, job_id: str) -> requests.Response:
        """
        Get a job by job ID.
        Similar to get_job. Returns a smaller payload than get_job. Incoming json variables are shortened to the
        Itential variables (ex $var.60d8.merged_object) as opposed to the entire json being passed into a task. This
        endpoint also excludes some meta data like: created, created_by, last_updated, last_updated_by, etc
        Response is about 20% lighter than get_job (scaling with task input sizes) (1535 vs 1873 lines for same job)
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getJobDetails/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/job/{job_id}/details")

    def get_job_from_task_query(self, task_query: str, options: Dict[str, Any]) -> requests.Response:
        """
        Search for jobs using a task query.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getJobFromTaskQuery/

        :param task_query: A mongodb query partial to run against the tasks to get the requested job.
         Examples: {"status": "running"}
        :param options: Sort, filter, and pagination options.
         Examples: {"filter": {"name": "<workflowName>"}, "page": {"skip": 0, "limit": 50}, "sort:
          {"field": "name", "direction": 1}}
        :return: requests.Response. A list of full job objects
        """
        body = {"task_query": task_query, "options": options}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/getJobFromTaskQuery", json=body)

    def get_job_list(
        self,
        status: str = "active",
        filters: Optional[Dict[str, str]] = None,
        limit: int = 10,
        skip: int = 0,
    ) -> requests.Response:
        """
        Get a list of jobs by status.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getJobList/

        :param filters: Ex: {"metrics.user": "admin@pronghorn"} to filter for a specific user.
        :param skip: Number of jobs to offset the result. Useful for pagination.
        :param status: Options: "active", "cancelled", "complete", "error", "incomplete", "paused", "running"
        :param limit: Set to 0 to disable pagination.
        :return: requests.Response
        """

        body = {
            "options": {
                "fields": {"tasks": 0},
                # filter: {"key.path": "value"}  Added below
                "page": {"skip": skip, "limit": limit},
                "sort": {"field": "name", "direction": -1},
            }
        }

        if filters:
            body["options"]["filter"] = filters

        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/getJobList/{status}", json=body)

    def get_job_output(self, job_id: str) -> requests.Response:
        """
        Get the output of a completed job.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getJobOutput/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/job/{job_id}/output")

    def get_job_shallow(self, job_id: str) -> requests.Response:
        """
        Get shallow data of a job by job ID. Returns a subset of data returned by omitting tasks' application, tasks'
        incoming arguments, tasks' returned data, and tasks' error information.
        About a 50% smaller payload than get_job (1535 vs 969)
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getJobShallow/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/getJobShallow/{job_id}")

    def get_job_visualization_data(self, job_id: str) -> requests.Response:
        """
        Get a job's visualization data by job ID.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getJobVisualizationData/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/jobs/visdata/{job_id}")

    def get_manual_task_controller(self, job_id: str, task_id: str) -> requests.Response:
        """
        Get a Manual Task's Controller (javascript function code)
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/getManualTaskController/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :param task_id: ID of the task associated with the controller

        :return: requests.Response. Contains incoming and outgoing variables, error, and "TaskController"
         javascript code
        """
        return self.client.call(
            method="GET", url=f"{self.client.url}/workflow_engine/tasks/controller/job/{job_id}/task/{task_id}"
        )

    def get_task(self, query: Dict[str, Any], filter: Dict[str, Any]) -> requests.Response:
        """
        Get the first Job's Task matching the query and return the data optionally modified by the filter.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/getTask/

        :param query: An object of property names and values to use in the query against the tasks collection.
         The property name must exist in the tasks collection. There must be at least 1 field you query upon.
         Ex: {"someFieldName": "value expected in field"}
        :param filter: Filter specifying which fields are returned. The structure of each property must conform to
         'fieldName': 1. Ex: {"name": 1} will return the name field

        :return: requests.Response.
        """
        body = {"query": query, "filter": filter}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/getTask", json=body)

    def get_task_details(self, location: str, package: str, method: str) -> requests.Response:
        """
        Get the detailed information model for a task. Documentation for this method is incomplete.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/getTaskDetails/

        :param location: Location: Application, Broker, Adapter
        :param package: Package name
        :param method: Method name

        :return: requests.Response.
         Ex: {
            "location": "Broker",
            "name": "query",
            "app": "WorkFlowEngine",
            "variables": {}
            }
        """
        return self.client.call(
            method="GET",
            url=f"{self.client.url}/workflow_engine/locations/{location}/packages/{package}/tasks/{method}",
        )

    def get_task_statuses(self, job_id: str) -> requests.Response:
        """
        Get the status of each Task in a job by job ID.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/getTaskStatuses/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"

        :return: requests.Response Statuses of all Tasks in the job.
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/job/statuses/{job_id}")

    def get_workflows_detailed_by_name(self, workflow_name: str) -> requests.Response:
        """
        Get the status of each Task in a job by job ID.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/getWorkflowsDetailedByName/

        :param workflow_name: Name of the workflow.
        :return: requests.Response Workflow details matching the Workflow name
        """
        return self.client.call(
            method="GET", url=f"{self.client.url}/workflow_engine/workflows/detailed/{workflow_name}"
        )

    def is_active(self) -> requests.Response:
        """
        Check if Staterator is currently active
        https://apidocs.itential.com/2020.2/api/-workflow_engine/isActive/

        :return: requests.Response Active flag for Staterator
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/active")

    def list_job_groups(self, job_id: str) -> requests.Response:
        """
        List the groups that have access to a job.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/listJobGroups/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response List of Group IDs.
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/jobs/{job_id}/groups")

    def pause_job(self, job_id: str) -> requests.Response:
        """
        Pause a job by job ID.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/pauseJob/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response Job after the pause.
        """
        body = {"job_id": job_id}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/pauseJob", json=body)

    def prepare_metrics_logs(self) -> requests.Response:
        """
        Compress the metrics logs directory for Jobs and return the link to download it.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/prepareMetricsLogs/

        :return: requests.Response URL containing the compressed job metrics zipped file
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_engine/metrics/jobs")

    def query_jobs(self, query: Dict[str, Any]) -> requests.Response:
        """
        Get jobs matching the query.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/queryJobs/

        :param query: An object of property names and values to use in the query against the jobs collection.
         The property name must exist in the jobs collection. There must be at least 1 field you query upon.
         Ex: {"query": {"someFieldName": "Some Value to query the against the someFieldName property"}}
        :return: requests.Response All jobs matching the query.
        """
        body = {"query": query}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/queryJobs", json=body)

    def query_tasks_brief(self, query: Dict[str, Any]) -> requests.Response:
        """
        Get brief information about task(s) from the tasks collection in mongoDB.
        This will return only tasks that are attached to a currently running Job
        https://apidocs.itential.com/2020.2/api/-workflow_engine/queryTasksBrief/

        :param query: An object of property names and values to use in the query against the jobs collection.
         The property name must exist in the jobs collection. There must be at least 1 field you query upon.
         Ex: {"query": {"someFieldName": "Some Value to query the against the someFieldName property"}}
        :return: requests.Response Jobs' Tasks matching the query.
        """
        body = {"query": query}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/queryTasksBrief", json=body)

    def release_task(self, task_id: str) -> requests.Response:
        """
        Get brief information about task(s) from the tasks collection in mongoDB.
        This will return only tasks that are attached to a currently running Job
        https://apidocs.itential.com/2020.2/api/-workflow_engine/releaseTask/

        :param task_id: ID of a specific task. Ex: "cd34"
        :return: requests.Response Task details after releasing the Task.
        """
        body = {"task_id": task_id}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/tasks/release", json=body)

    def remove_job_group(self, job_id: str, group_id: str) -> requests.Response:
        """
        Remove a group from the list of authorized groups for a job.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/removeJobGroup/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :param group_id: ID of a group. Ex:
        :return: requests.Response Status of the removal of a group from a job.
        """
        return self.client.call(
            method="DELETE", url=f"{self.client.url}/workflow_engine/jobs/{job_id}/groups/{group_id}"
        )

    def replace_job_groups(self, job_id: str, group_list: List[str]) -> requests.Response:
        """
        Overwrite the list of groups that have access to a job.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/replaceJobGroups/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :param group_list: List of group IDs
        :return: requests.Response Status of the removal of a group from a job.
        """
        body = {"groups": group_list}
        return self.client.call(method="PUT", url=f"{self.client.url}/workflow_engine/jobs/{job_id}/groups", json=body)

    def resume_job(self, job_id: str) -> requests.Response:
        """
        Resume a paused or errored job by job ID.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/resumeJob/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response Job after the resume.
        """
        body = {"job_id": job_id}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/resumeJob", json=body)

    def revert_to_task(self, job_id: str, current_task_id: str, target_task_id: str) -> requests.Response:
        """
        Revert a job from current Task to the target task by job ID and task names.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/revertToTask/

        :param job_id: Returned when creating a job or querying for jobs by workflow name.
         Ex: "ec59ef85fef84e59bf36bd1e"
        :param current_task_id: Name of the current Task.
        :param target_task_id: Name of the Target Task.
        :return: requests.Response Job after the revert.
        """
        body = {"job_id": job_id, "current_task": current_task_id, "target_task": target_task_id}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/revertToTask", json=body)

    def run_evaluation_group(self, evaluation_group: List[Dict[str, Any]], all_true_flag: bool) -> requests.Response:
        """
        Run a test evaluation.
        Note: This might be an accidentally exposed endpoint for the "evaluation" task within a workflow.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/runEvaluationGroup/

        :param evaluation_group: Array of evaluations to run
        :param all_true_flag: All evaluation groups must pass, or not
        :return: requests.Response Result of evaluation.
        Ex:
            {
              "evaluation_group": [
                {
                  "operand_1": 47978204.94549683,
                  "operator": "contains",
                  "operand_2": 95772920.69505993,
                  "query": "somePropertyNameInOperand_1IfItIsAnObject"
                },
                {
                  "operand_1": [],
                  "operator": "contains",
                  "query": "somePropertyNameInOperand_1IfItIsAnObject"
                }
              ],
              "all_true_flag": true
            }
        """
        body = {
            "evaluation_group": evaluation_group,
            "all_true_flag": all_true_flag,
        }
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/runEvaluationGroup", json=body)

    def run_evaluation_groups(self, evaluation_group: List[Dict[str, Any]], all_true_flag: bool) -> requests.Response:
        """
        Run a test evaluation.
        Note: This might be an accidentally exposed endpoint for the "evaluation" task within a workflow.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/runEvaluationGroups/

        :param evaluation_group: Array of evaluations to run
        :param all_true_flag: All evaluation groups must pass, or not
        :return: requests.Response Result of evaluation.
        Ex:
            {
              "evaluation_group": [
                {
                  "evaluations": [
                    {
                      "operand_1": true,
                      "operator": "contains",
                      "operand_2": "Lorem veniam",
                      "query": "somePropertyNameInOperand_1IfItIsAnObject"
                    },
                    {
                      "operand_1": [],
                      "operator": "contains",
                      "operand_2": -18752418,
                      "query": "somePropertyNameInOperand_1IfItIsAnObject"
                    }
                  ],
                  "all_true_flag": true
                }
              ],
              "all_true_flag": true
            }
        """
        body = {
            "evaluation_group": evaluation_group,
            "all_true_flag": all_true_flag,
        }
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/runEvaluationGroups", json=body)

    def run_validation(self, workflow_json: Dict[str, Any]) -> requests.Response:
        """
        Validate a workflow, and return the resulting errors and warnings arrays.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/runValidation/

        :param workflow_json: The workflow object to run validations against.
        :return: requests.Response Errors and warnings output from the validation process
        """
        body = {"workflow": workflow_json}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/workflows/validate", json=body)

    def search_jobs(
        self,
        expand: Optional[List[str]] = None,
        query: Optional[Dict[str, str]] = None,
        fields: Optional[Dict[str, int]] = None,
        local: Optional[bool] = True,
        sort: Optional[Dict[str, int]] = None,
        limit: int = 0,
        skip: int = 0,
    ) -> requests.Response:
        """
        TODO: Needs testing to identify what each param actually means. Documentation is very lacking.
        Search jobs with Options. This is similar to search_workflows, but with some additional fields.
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/searchJobs/

        :param expand: {"expand": ["user"]}.
        :param query: {"name": "workflow_name"}. "name" field can be any field in the workflow json.
        :param fields: {"name": 1}. "name" field can be any field in the workflow json.
         Used to filter out other fields
        :param sort: {"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
        :param limit: Max results to return
        :param local:
        :param skip: Number to offset the search by
        :return: requests.Response example json(): Search Results: {"results": ["_id": int, "name": str], "skip": int,
         "limit": int, "total": int}
        Ex: {
              "options": {
                "expand": [
                  "user",
                  "owner",
                  "owner",
                  "user"
                ],
                "fields": {
                  "name": 1
                },
                "query": {
                  "name": "abcd"
                },
                "limit": 50,
                "local": true,
                "skip": 0,
                "sort": {
                  "name": -1
                }
              }
            }
        """

        data = {"options": {"fields": {"name": 1}, "limit": limit, "local": local, "skip": skip, "sort": {"name": 1}}}

        if query:
            data["options"]["query"] = query

        if expand:
            data["options"]["expand"] = expand

        if fields:
            data["options"]["fields"] = fields

        if sort:
            data["options"]["sort"] = sort

        return self.client.call(method="POST", url=rf"{self.client.url}/workflow_engine/jobs/search", json=data)

    def search_tasks(
        self,
        filter: Dict[str, Any],
        expand: Optional[List[str]] = None,
        query: Optional[Dict[str, str]] = None,
        fields: Optional[Dict[str, int]] = None,
        local: Optional[bool] = True,
        sort: Optional[Dict[str, int]] = None,
        limit: int = 0,
        skip: int = 0,
    ) -> requests.Response:
        """
        TODO: Needs testing to identify what each param actually means. Documentation is very lacking.
        Search jobs with Options.
        Note: Unique in that it has an additional parameter "filter".
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/searchTasks/

        :param filter: Search Filter Ex: {"someFieldName": "Some Value to query the against the someFieldName property"}
        :param expand: {"expand": ["user"]}.
        :param query: {"name": "workflow_name"}. "name" field can be any field in the workflow json.
        :param fields: {"name": 1}. "name" field can be any field in the workflow json.
         Used to filter out other fields
        :param sort: {"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
        :param limit: Max results to return
        :param local:
        :param skip: Number to offset the search by
        :return: requests.Response example json(): Search Results: {"results": ["_id": int, "name": str], "skip": int,
         "limit": int, "total": int}
        Ex: {
              "filter": {
                "someFieldName": "Some Value to query the against the someFieldName property"
              },
              "options": {
                "expand": [
                  "owner",
                  "owner",
                  "created_by",
                  "owner",
                  "owner"
                ],
                "fields": {
                  "name": 1
                },
                "query": {
                  "name": "abcd"
                },
                "limit": 50,
                "local": false,
                "skip": 0,
                "sort": {
                  "name": -1
                }
              }
            }
        """

        data = {
            "filter": filter,
            "options": {"fields": {"name": 1}, "limit": limit, "local": local, "skip": skip, "sort": {"name": 1}},
        }

        if query:
            data["options"]["query"] = query

        if expand:
            data["options"]["expand"] = expand

        if fields:
            data["options"]["fields"] = fields

        if sort:
            data["options"]["sort"] = sort

        return self.client.call(method="POST", url=rf"{self.client.url}/workflow_engine/tasks/search", json=data)

    def search_workflows(
        self,
        query: Optional[Dict[str, str]] = None,
        fields: Optional[Dict[str, int]] = None,
        sort: Optional[Dict[str, int]] = None,
        limit: int = 0,
        skip: int = 0,
    ) -> requests.Response:
        """
        Search Workflows with Options
        https://apidocs.itential.com/2020.2/api/app-workflow_engine/searchWorkflows/

        :param query: {"name": "workflow_name"}. "name" field can be any field in the workflow json.
        :param fields: {"name": 1}. "name" field can be any field in the workflow json.
         Used to filter out other fields
        :param sort: {"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
        :param limit: Max results to return
        :param skip: Number to offset the search by
        :return: requests.Response example json(): {"results": ["_id": int, "name": str], "skip": int,
         "limit": int, "total": int}
        """

        data = {"options": {"fields": {"name": 1}, "limit": limit, "skip": skip, "sort": {"name": 1}}}

        if query:
            data["options"]['query'] = query

        if fields:
            data["options"]["fields"] = fields

        if sort:
            data["options"]["sort"] = sort

        return self.client.call(method="POST", url=rf"{self.client.url}/workflow_engine/workflows/search", json=data)

    def unwatch_job(self, job_id: str) -> requests.Response:
        """
        Remove the current user from the watchers list of a job.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/unwatchJob/

        :param job_id: ID of the job
        :return: requests.Response User id removed from the watchers list.
        """
        return self.client.call(method="DELETE", url=f"{self.client.url}/workflow_engine/job/{job_id}/watch")

    def validate_all_loops(self, workflow_json: Dict[str, Any]) -> requests.Response:
        """
        Validate all looped Tasks in a Workflow by Workflow details.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/validateAllLoops/

        :param workflow_json: Full workflow json/dict
        :return: requests.Response User id removed from the watchers list.
        """
        body = {"workflow_details": workflow_json}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_engine/validateAllLoops", json=body)

    def watch_job(self, job_id: str) -> requests.Response:
        """
        Add current user to a job's watchers list.
        https://apidocs.itential.com/2020.2/api/-workflow_engine/watchJob/

        :param job_id: ID of the job
        :return: requests.Response User id added to the watchers list.
        """
        return self.client.call(method="PUT", url=f"{self.client.url}/workflow_engine/job/{job_id}/watch")
