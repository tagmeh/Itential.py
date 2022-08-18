"""
Link to Itential Docs: https://docs.itential.com/2020.2/api/app-workflow_engine/

Implemented  Doc String  Tests
    [x]         [x]       [ ]   activate
    [-]         [-]       [-]   addDuration
    [x]         [x]       [ ]   addWatchers
    [-]         [-]       [-]   arrayConcat
    [-]         [-]       [-]   arrayIncludes
    [-]         [-]       [-]   arrayIndexOf
    [-]         [-]       [-]   arrayLastIndexOf
    [-]         [-]       [-]   arrayLength
    [-]         [-]       [-]   arrayPop
    [-]         [-]       [-]   arrayPush
    [-]         [-]       [-]   arrayShift
    [-]         [-]       [-]   arraySlice
    [-]         [-]       [-]   arrayToLocaleString
    [-]         [-]       [-]   arrayToString
    [-]         [-]       [-]   assign
    [-]         [-]       [-]   calculateTimeDiff
    [x]         [x]       [ ]   cancelJob
    [-]         [-]       [-]   charAt
    [-]         [-]       [-]   charCodeAt
    [x]         [x]       [ ]   checkWorkflowForJobVariables
    [-]         [-]       [-]   childJob
    [x]         [x]       [-]   claimTask
    [-]         [-]       [-]   codePointAt
    [-]         [-]       [-]   convertEpochToObject
    [-]         [-]       [-]   convertTimeFormat
    [-]         [-]       [-]   convertTimeToEpoch
    [-]         [-]       [-]   convertTimezone
    [-]         [-]       [-]   copyWithin
    [x]         [x]       [ ]   createJobGroupEntry
    [x]         [x]       [ ]   deactivate
    [-]         [-]       [-]   decision
    [-]         [-]       [-]   deepmerge
    [-]         [-]       [-]   delay
    [x]         [x]       [ ]   deleteJobGroups
    [x]         [x]       [ ]   diffToHTML
    [-]         [-]       [-]   endsWith
    [-]         [-]       [-]   ErrorHandling
    [-]         [-]       [-]   evaluation
    [-]         [-]       [-]   eventListenerJob
    [-]         [-]       [-]   extractField
    [-]         [-]       [-]   fill
    [x]         [x]       [ ]   find
    [x]         [x]       [ ]   findForwardPaths
    [x]         [x]       [ ]   finishManualTask
    [x]         [x]       [ ]   fixJob
    [-]         [-]       [-]   FlattenJSONFormInput
    [-]         [-]       [-]   forEach
    [-]         [-]       [-]   getAllLoopTasks
    [x]         [x]       [ ]   getAssociatedJobs
    [ ]         [ ]       [ ]   getEntireJob
    [ ]         [ ]       [ ]   getJob
    [ ]         [ ]       [ ]   getJobDetails
    [ ]         [ ]       [ ]   getJobFromTaskQuery
    [x]         [x]       [ ]   getJobList
    [x]         [x]       [ ]   getJobOutput
    [ ]         [ ]       [ ]   getJobShallow
    [ ]         [ ]       [ ]   getJobVisualizationData
    [ ]         [ ]       [ ]   getManualTaskController
    [ ]         [ ]       [ ]   getTask
    [ ]         [ ]       [ ]   getTaskDetails
    [ ]         [ ]       [ ]   getTaskStatuses
    [ ]         [ ]       [ ]   getTime
    [ ]         [ ]       [ ]   getWorkflowsDetailedByName
    [ ]         [ ]       [ ]   isActive
    [ ]         [ ]       [ ]   isArray
    [ ]         [ ]       [ ]   join
    [ ]         [ ]       [ ]   keys
    [ ]         [ ]       [ ]   listJobGroups
    [ ]         [ ]       [ ]   localeCompare
    [ ]         [ ]       [ ]   makeData
    [ ]         [ ]       [ ]   map
    [ ]         [ ]       [ ]   match
    [ ]         [ ]       [ ]   merge
    [ ]         [ ]       [ ]   modify
    [ ]         [ ]       [ ]   newVariable
    [ ]         [ ]       [ ]   normalize
    [ ]         [ ]       [ ]   numberToString
    [ ]         [ ]       [ ]   objectHasOwnProperty
    [ ]         [ ]       [ ]   objectToString
    [ ]         [ ]       [ ]   padEnd
    [ ]         [ ]       [ ]   padStart
    [ ]         [ ]       [ ]   parse
    [ ]         [ ]       [ ]   parseInt
    [ ]         [ ]       [ ]   pauseJob
    [ ]         [ ]       [ ]   pop
    [ ]         [ ]       [ ]   prepareMetricsLogs
    [ ]         [ ]       [ ]   push
    [ ]         [ ]       [ ]   query
    [ ]         [ ]       [ ]   queryJobs
    [ ]         [ ]       [ ]   queryTasksBrief
    [ ]         [ ]       [ ]   releaseTask
    [ ]         [ ]       [ ]   removeJobGroup
    [ ]         [ ]       [ ]   repeat
    [ ]         [ ]       [ ]   replace
    [ ]         [ ]       [ ]   replaceJobGroups
    [ ]         [ ]       [ ]   restCall
    [ ]         [ ]       [ ]   resumeJob
    [ ]         [ ]       [ ]   reverse
    [ ]         [ ]       [ ]   revertToTask
    [ ]         [ ]       [ ]   runEvaluationGroup
    [ ]         [ ]       [ ]   runEvaluationGroups
    [ ]         [ ]       [ ]   runValidation
    [ ]         [ ]       [ ]   search
    [ ]         [ ]       [ ]   searchJobs
    [ ]         [ ]       [ ]   searchTasks
    [ ]         [ ]       [ ]   searchWorkflows
    [ ]         [ ]       [ ]   setObjectKey
    [ ]         [ ]       [ ]   shift
    [ ]         [ ]       [ ]   sort
    [ ]         [ ]       [ ]   split
    [ ]         [ ]       [ ]   startJobWithOptions
    [ ]         [ ]       [ ]   startsWith
    [ ]         [ ]       [ ]   stringConcat
    [ ]         [ ]       [ ]   stringIncludes
    [ ]         [ ]       [ ]   stringIndexOf
    [ ]         [ ]       [ ]   stringLastIndexOf
    [ ]         [ ]       [ ]   stringLength
    [ ]         [ ]       [ ]   stringSlice
    [ ]         [ ]       [ ]   stringValueOf
    [ ]         [ ]       [ ]   stub
    [ ]         [ ]       [ ]   substring
    [ ]         [ ]       [ ]   toLocaleLowerCase
    [ ]         [ ]       [ ]   toLocaleUpperCase
    [ ]         [ ]       [ ]   toLowerCase
    [ ]         [ ]       [ ]   toUpperCase
    [ ]         [ ]       [ ]   transformation
    [ ]         [ ]       [ ]   trim
    [ ]         [ ]       [ ]   trimEnd
    [ ]         [ ]       [ ]   trimStart
    [ ]         [ ]       [ ]   unshift
    [ ]         [ ]       [ ]   unwatchJob
    [ ]         [ ]       [ ]   updateJobDescription
    [ ]         [ ]       [ ]   validateAllLoops
    [ ]         [ ]       [ ]   values
    [ ]         [ ]       [ ]   ViewData
    [ ]         [ ]       [ ]   ViewDiff
    [ ]         [ ]       [ ]   watchJob
"""
import warnings
from typing import TYPE_CHECKING, Optional, Dict, Any, List

import requests

if TYPE_CHECKING:
    from itential.core import Itential


class AppWorkflowEngine:
    """https://docs.itential.com/2020.2/api/app-workflow_engine/"""

    @staticmethod
    def activate(client: "Itential", **kwargs: Dict[str, Any]) -> requests.Response:
        """
        Activate Task Worker ( API payload not documented. May not be usable/implemented )
        https://docs.itential.com/2020.2/api/app-workflow_engine/activate/
        :param client: The Itential state object
        :param kwargs: Undocumented payload kwargs
        :return: Status flag of activation
        """
        return client.call(method="POST", url=f"{client.url}/workflow_engine/activate", json=kwargs)

    @staticmethod
    def add_watchers(client: "Itential", job_id: str, watchers: List[str]) -> requests.Response:
        """
        Add users to the watchers list of a job by job ID and username.
        https://docs.itential.com/2020.2/api/app-workflow_engine/addWatchers/
        :param client: The Itential state object
        :param job_id: ID of the job to watch.
        :param watchers: Users to add to watchers list.
        :return: User IDs added to the watchers list.
        """
        body = {"job_id": job_id, "watchers": watchers}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/job/watchers/watch", json=body)

    @staticmethod
    def cancel_job(client: "Itential", job_id: str) -> requests.Response:
        """
        Cancel an active job by job ID.
        https://docs.itential.com/2020.2/api/app-workflow_engine/cancelJob/
        :param client: The Itential state object
        :param job_id: ID of the job to cancel.
        :return: Data from the canceled job.
        """
        body = {"job_id": job_id}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/cancelJob", json=body)

    @staticmethod
    def check_workflow_for_job_variables(client: "Itential", workflow_name: str) -> requests.Response:
        """
        Get job variables of a workflow by workflow name.
        https://docs.itential.com/2020.2/api/app-workflow_engine/checkWorkflowForJobVariables/
        :param client: The Itential state object
        :param workflow_name: Name of the workflow.
        :return: Variables of the workflow matching the name.
        """
        return client.call(method="GET", url=f"{client.url}/workflow_engine/workflows/variables/{workflow_name}")

    @staticmethod
    def claim_task(client: "Itential", task_id: str, user: str) -> requests.Response:
        """
        Claim a manual Task
        https://docs.itential.com/2020.2/api/app-workflow_engine/claimTask/
        :param client: The Itential state object
        :param task_id: ID of the Task to claim.
        :param user: User id for the user claiming the Task.
        :return: Result of claiming the Task.
        """
        body = {"task_id": task_id, "user": user}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/tasks/claim", json=body)

    @staticmethod
    def create_job_group_entry(client: "Itential", job_id: str, group_id: str) -> requests.Response:
        """
        Add a group to the list of groups for a job.
        https://docs.itential.com/2020.2/api/app-workflow_engine/createJobGroupEntry/
        :param client: The Itential state object
        :param job_id: ID of job
        :param group_id: A Group id
        :return: Status of adding a group to a job.
        """
        body = {"group": group_id}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/jobs/{job_id}/groups", json=body)

    @staticmethod
    def deactivate(client: "Itential", **kwargs: Dict[str, Any]) -> requests.Response:
        """
        Deactivate Task Worker ( API payload not documented. May not be usable/implemented )
        https://docs.itential.com/2020.2/api/app-workflow_engine/deactivate/
        :param client: The Itential state object
        :param kwargs: Undocumented POST payload
        :return: Status flag of deactivation
        """
        return client.call(method="POST", url=f"{client.url}/workflow_engine/deactivate", json=kwargs)

    @staticmethod
    def delete_job_groups(client: "Itential", job_id: str) -> requests.Response:
        """
        Remove all authorization restriction for a job.
        https://docs.itential.com/2020.2/api/app-workflow_engine/deleteJobGroups/
        :param client: The Itential state object
        :param job_id: ID of job
        :return: Status of Delete
        """
        return client.call(method="DELETE", url=f"{client.url}/workflow_engine/jobs/{job_id}/groups")

    @staticmethod
    def diff_to_html(client: "Itential", label1: str, value1: str, label2: str, value2: str) -> requests.Response:
        """
        DEPRECIATED: Difference between two values in HTML response
        https://docs.itential.com/2020.2/api/app-workflow_engine/diffToHTML/
        :param client: The Itential state object
        :param label1: Optional label for value1
        :param value1: Any value to diff against value2
        :param label2: Optional label for value2
        :param value2: Any value to diff against value1
        :return: HTML difference between value1 and value2
        """
        warnings.warn("Marked as depreciated by Itential.", PendingDeprecationWarning)
        body = {"label1": label1, "value1": value1, "label2": label2, "value2": value2}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/diffToHTML", json=body)

    @staticmethod
    def find(client: "Itential", query: Dict[str, Any], options: Dict[str, Any]) -> requests.Response:
        """
        Find job Documents based on a query and additional options.
        https://docs.itential.com/2020.2/api/app-workflow_engine/find/
        :param client: The Itential state object
        :param query: A MongoDB query object. See docs for an example
        :param options: A MongoDB options object. See docs for an example
        :return: Resulting job Documents that matched query and options.
        """
        body = {"query": query, "options": options}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/jobs/find", json=body)

    @staticmethod
    def find_forward_paths(
        client: "Itential", start_task_id: str, end_task_id: str, workflow_details: Dict[str, Any]
    ) -> requests.Response:
        """
        Find the paths between two Tasks in a Workflow by Task ids and Workflow details.
        https://docs.itential.com/2020.2/api/app-workflow_engine/findForwardPaths/
        :param client: The Itential state object
        :param start_task_id: ID of the start Task.
        :param end_task_id: ID of the end Task.
        :param workflow_details: Workflow data which contain the tasks and transitions properties of the workflow.
        :return: All valid paths between the Tasks.
        """
        body = {"start_task": start_task_id, "end_task": end_task_id, "workflow_details": workflow_details}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/findForwardPaths", json=body)

    @staticmethod
    def finish_manual_task(
        client: "Itential", task_id: str, job_id: str, task_data: Dict[str, Any]
    ) -> requests.Response:
        """
        Finishes a manual task with finish state success
        https://docs.itential.com/2020.2/api/app-workflow_engine/finishManualTask/
        :param client: The Itential state object
        :param task_id: ID of the Task within that job.
        :param job_id: ID of the Job.
        :param task_data: Data of the completed Task.
        :return: The Current Job Object
        """
        body = {"task_id": task_id, "job_id": job_id, "task_data": task_data}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/finishTask", json=body)

    @staticmethod
    def fix_job(client: "Itential", job_id: str, errored_task: str, revert_task: str) -> requests.Response:
        """
        Revert an errored job to a target task by job ID and task names.
        https://docs.itential.com/2020.2/api/app-workflow_engine/fixJob/
        :param client: The Itential state object
        :param job_id: ID of the job to fix.
        :param errored_task: Name of the errored Task.
        :param revert_task: Name of the target Task.
        :return: Job after the revert.
        """
        body = {"job_id": job_id, "errored_task": errored_task, "revert_task": revert_task}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/fixJob", json=body)

    @staticmethod
    def get_all_loop_tasks(client: "Itential", workflow_details: Dict[str, Any]) -> requests.Response:
        """
        Get all looped Tasks in a Workflow by Workflow details.
        https://docs.itential.com/2020.2/api/app-workflow_engine/getAllLoopTasks/
        :param client: The Itential state object
        :param workflow_details: Workflow to get looped tasks.
        :return: looped Tasks of the Workflow.
        """
        body = {"workflow_details": workflow_details}
        return client.call(method="POST", url=f"{client.url}/workflow_engine/getAllLoopTasks", json=body)

    @staticmethod
    def get_associated_jobs(
        client: "Itential",
        filters: Optional[Dict[str, str]] = None,
        sort: Optional[Dict[str, int]] = None,
        limit: int = 10,
        skip: int = 0,
    ) -> requests.Response:
        """
        Search for jobs that the user has touched.
        https://docs.itential.com/2020.2/api/app-workflow_engine/getAssociatedJobs/
        :param client: The Itential state object
        :param filters: Ex: {"metrics.user": "admin@pronghorn"} to filter for a specific user.
        :param skip: Number of jobs to offset the result. Useful for pagination.
        :param sort:{"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
        :param limit: Set to 0 to disable pagination.
        :return: All matching jobs. example json(): {"results": ["_id": int, "name": str], "skip": int,
                                                    "limit": int, "total": int}
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

        return client.call(method="POST", url=f"{client.url}/workflow_engine/getAllLoopTasks", json=body)

    @staticmethod
    def get_job_list(
        client: "Itential",
        status: str = "active",
        filters: Optional[Dict[str, str]] = None,
        limit: int = 10,
        skip: int = 0,
    ) -> requests.Response:
        """
        Get a list of jobs by status
        https://docs.itential.com/2020.2/api/app-workflow_engine/getJobList/
        :param client: The Itential client state object, required for authentication with the server.
        :param filters: Ex: {"metrics.user": "admin@pronghorn"} to filter for a specific user.
        :param skip: Number of jobs to offset the result. Useful for pagination.
        :param status: Options: "active", "cancelled", "complete", "error", "incomplete", "paused", "running"
        :param limit: Set to 0 to disable pagination.
        :return: requests.Response
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

        return client.call(method="POST", url=f"{client.url}/workflow_engine/getJobList/{status}", json=body)

    @staticmethod
    def get_job_output(client: "Itential", job_id: str) -> requests.Response:
        """
        Get the output of a completed job.
        https://docs.itential.com/2020.2/api/app-workflow_engine/getJobOutput/
        :param client: Itential client object. Passed in to all commands
        :param job_id: Returned when creating a job or querying for jobs by workflow name. Ex: "ec59ef85fef84e59bf36bd1e"
        :return: requests.Response
        """
        return client.call(method="GET", url=f"{client.url}/workflow_engine/job/{job_id}/output")

    @staticmethod
    def search_workflows(
        client: "Itential",
        query: Optional[Dict[str, str]] = None,
        fields: Optional[Dict[str, int]] = None,
        sort: Optional[Dict[str, int]] = None,
        limit: int = 0,
        skip: int = 0,
    ) -> requests.Response:
        """
        Search Workflows with Options
        https://docs.itential.com/2020.2/api/app-workflow_engine/searchWorkflows/
        :param client: The Itential client state object
        :param query: {"name": "workflow_name"}. "name" field can be any field in the workflow json.
        :param fields: {"name": 1}. "name" field can be any field in the workflow json.
            Used to filter out other fields
        :param sort:{"name": -1} or {"name": 1}. "name" field can be any field in the workflow json.
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

        return client.call(method="POST", url=rf"{client.url}/workflow_engine/workflows/search", json=data)


if __name__ == '__main__':
    AppWorkflowEngine.diff_to_html()
