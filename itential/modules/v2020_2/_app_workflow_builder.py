"""
Link to Itential Docs: https://apidocs.itential.com/2020.2/api/app-workflow_builder/

Implemented  Doc String  Tests
    [x]         [x]       [ ]   createWorkflowGroupEntry
    [x]         [x]       [ ]   deleteWorkflow
    [x]         [x]       [ ]   deleteWorkflowGroups
    [x]         [x]       [ ]   exportWorkflow
    [x]         [x]       [ ]   getSchemas
    [x]         [x]       [ ]   getTaskDetails
    [x]         [x]       [ ]   getTasksList
    [x]         [x]       [ ]   importWorkflow
    [x]         [x]       [ ]   listWorkflowGroups
    [x]         [x]       [ ]   removeWorkflowGroup
    [x]         [x]       [ ]   renameWorkflow
    [x]         [x]       [ ]   replaceWorkflowGroups
    [x]         [x]       [ ]   saveWorkflow
"""
from typing import TYPE_CHECKING, Dict, List, Any

if TYPE_CHECKING:
    import requests
    from itential.core import Itential


class AppWorkflowBuilder:
    """
    https://apidocs.itential.com/2020.2/api/app-workflow_builder/
    """

    def __init__(self, client: "Itential"):
        self.client = client

    def delete_workflow(self, name: str) -> "requests.Response":
        """
        Deletes a single workflow of the given name.
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/deleteWorkflow/

        :param name: Name of the workflow to be deleted.
        :return: requests.Response object
                 A successful delete returns the deleted workflow json.
                 A failed delete returns a 500: "TypeError: Cannot read property '_id' of null"
        """
        return self.client.call(method="DELETE", url=f"{self.client.url}/workflow_builder/workflows/delete/{name}")

    def import_workflow(self, data: Dict[str, Any]) -> "requests.Response":
        """
        Imports a single workflow.
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/importWorkflow/

        :param data: The workflow json object.
        :return: requests.Response object. Successful response ex: {'n': 1, 'ok': 1, 'name': 'automation_name'}
        """
        data = {"workflow": data, "options": {}}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_builder/import", json=data)

    def create_workflow_group_entry(self, workflow_name: str, group_name: str) -> "requests.Response":
        """
        Add Group to a Workflow.
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/createWorkflowGroupEntry/

        :param workflow_name: Name of the workflow to be assigned to the group
        :param group_name: < Unclear atm. Docs show an id, but the description says "name".
        :return: requests.Response
                                    500 error: "Invalid group: TestGroupName"
        """
        data = {"group": group_name}
        return self.client.call(
            method="POST", url=f"{self.client.url}/workflow_builder/workflows/{workflow_name}/groups", json=data
        )

    def delete_workflow_groups(self, workflow_name: str, group_name: str) -> "requests.Response":
        """
        Delete all Groups for a Workflow
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/deleteWorkflowGroups/ (Docs are incomplete)

        :param workflow_name: Name of the workflow to delete
        :param group_name: < unclear atm > Itential docs aren't complete for this version.
        :return: requests.Response  200: boolean
                                    500: "Could not find workflow: TestWorkflow". The group_name doesn't seem to matter.
        """
        data = {'groups': group_name}
        return self.client.call(
            method="DELETE", url=f"{self.client.url}/workflow_builder/workflows/{workflow_name}/groups", json=data
        )

    def export_workflow(self, workflow_id: str = '', workflow_name: str = '') -> "requests.Response":
        """
        Returns the workflow json (Does not include a "_id" key at the top level)
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/exportWorkflow/

        :param workflow_id: ID of the workflow to export
        :param workflow_name: Name of the workflow to export.
        :return: requests.Response  200: Returns the full workflow json.
                Wrong workflow name 500: "Could not find matching workflow"
                Wrong workflow ID   500: "Could not find matching workflow"
        """
        data = {'options': {"type": "automation"}}  # "type" is optional

        if workflow_id:
            data["options"]["_id"] = workflow_id

        elif workflow_name:
            data["options"]["name"] = workflow_name

        else:
            raise AttributeError("Must have one of 'workflow_id' or 'workflow_name'.")

        return self.client.call(method="POST", url=f"{self.client.url}/workflow_builder/export", json=data)

    def get_schemas(self, workflow_object: Dict[str, Any]) -> "requests.Response":
        """
        Calculate incoming/outgoing schemas for the workflow
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/getSchemas/

        :param workflow_object: A workflow json object.
        :return: requests.Response  200: {"inputSchema": {...}, "outputSchema": {...}}
        """
        data = {"workflow": workflow_object}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_builder/workflows/schemas", json=data)

    def get_task_details(self, app_name: str, task_id: str) -> "requests.Response":
        """
        Get Task Details
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/getTaskDetails/

        :param app_name: Application Name (Export field in model)
        :param task_id: Task ID (Hexadecimal). < Unclear what this variable is >
        :return: requests.Response  200:
        """
        return self.client.call(method="GET", url=f"{self.client.url}/getTaskDetails/{app_name}/{task_id}")

    def get_tasks_list(self) -> "requests.Response":
        """
        Get all Tasks.
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/getTasksList/

        :return: requests.Response
        """
        return self.client.call(method="GET", url=f"{self.client.url}/workflow_builder/tasks/list")

    def list_workflow_groups(self, workflow_name: str) -> "requests.Response":
        """
        List the groups that have access to a Workflow
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/listWorkflowGroups/

        :param workflow_name: Name of the workflow to query
        :return: requests.Response
        """
        return self.client.call(
            method="GET", url=f"{self.client.url}/workflow_builder/workflows/{workflow_name}/groups"
        )

    def remove_workflow_group(self, workflow_name: str, group_name: str) -> "requests.Response":
        """
        Remove a group from the list of authorized groups for a Workflow
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/removeWorkflowGroup/

        :param workflow_name: Name of workflow to remove group from
        :param group_name: Name of group to remove from workflow.
        :return: requests.Response
        """
        return self.client.call(
            method="DELETE", url=f"{self.client.url}/workflow_builder/workflows/{workflow_name}/groups/{group_name}"
        )

    def rename_workflow(self, workflow_object: Dict[str, Any], new_name: str) -> "requests.Response":
        """
        Rename a Workflow in the database
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/renameWorkflow/

        :param workflow_object: Current workflow object. Minimum requirements are {"_id": "", "name": ""}
        :param new_name: New workflow name.
        :return: requests.Response
        """
        data = {"workflow": workflow_object, "newName": new_name}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_builder/workflows/rename", json=data)

    def replace_workflow_groups(self, workflow_name: str, group_list: List[str]) -> "requests.Response":
        """
        Overwrite the list of groups that have access to a Workflow
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/replaceWorkflowGroups/

        :param workflow_name: Name of the workflow
        :param group_list: List of group IDs (Hexadecimal)
        :return: requests.Response
        """
        data = {"groups": group_list}
        return self.client.call(
            method="PUT", url=f"{self.client.url}/workflow_builder/workflows/{workflow_name}/groups/", json=data
        )

    def save_workflow(self, workflow_obj: Dict[str, Any]) -> "requests.Response":
        """
        Add a Workflow to the database (Basically the save button)
        https://apidocs.itential.com/2020.2/api/app-workflow_builder/saveWorkflow/

        :param workflow_obj: Full workflow json
        :return: requests.Response
        """
        data = {"workflow": workflow_obj}
        return self.client.call(method="POST", url=f"{self.client.url}/workflow_builder/workflows/save", json=data)
