"""
Link to Itential Docs: https://apidocs.itential.com/2020.2/api/app-automation_catalog/

Implemented  Doc String  Tests
    [x]         [x]       [ ]   createAutomation
    [x]         [x]       [ ]   deleteAutomations
    [x]         [x]       [ ]   exportAutomation
    [x]         [x]       [ ]   getAutomationById
    [x]         [x]       [ ]   getAutomations
    [x]         [x]       [ ]   importAutomations
    [x]         [x]       [ ]   migrateAgendaJobs
    [x]         [x]       [ ]   runAutomation
    [x]         [x]       [ ]   updateAutomation
"""
from typing import TYPE_CHECKING, List, Dict, Any

if TYPE_CHECKING:
    from itential.core import Itential
    import requests


class AppAutomationCatalog:
    """https://apidocs.itential.com/2020.2/api/app-automation_catalog/"""

    def __init__(self, client: "Itential"):
        self.client = client

    def create_automation(self, name: str, description: str) -> "requests.Response":
        """
        Creates an automation with optional description.
        An automation's root structure is based off the agenda.js library,
         with any custom data falling into the 'data' array
        https://apidocs.itential.com/2020.2/api/app-automation_catalog/createAutomation/

        :param name: Unique name of the automation
        :param description: Short description of the automation
        :return: requests.Response: Automation document that was created by the request
        """
        body = {"name": name, "description": description}
        return self.client.call(method="POST", url=f"{self.client.url}/automation_catalog/automations", json=body)

    def delete_automations(self, ids: List[str]) -> "requests.Response":
        """
        Deletes automations (based off an array of Ids)
        https://apidocs.itential.com/2020.2/api/app-automation_catalog/deleteAutomations/

        :param ids: List of automation IDs
        :return: requests.Response: Object containing a property removeCount
        """
        body = {"ids": ids}
        return self.client.call(method="DELETE", url=f"{self.client.url}/automation_catalog/automations", json=body)

    def export_automations(self, automation_id: str) -> "requests.Response":
        """
        Returns a single automation formatted for importing
        https://apidocs.itential.com/2020.2/api/app-automation_catalog/exportAutomation/

        :param automation_id: Unique id of the automation
        :return: requests.Response: Automation document that was requested in exported format
        """
        return self.client.call(
            method="GET", url=f"{self.client.url}/automation_catalog/automations/{automation_id}/export"
        )

    def get_automation_by_id(self, automation_id: str) -> "requests.Response":
        """
        Gets an single automation by its id
        https://apidocs.itential.com/2020.2/api/app-automation_catalog/getAutomationById/

        :param automation_id: Unique id of the automation
        :return: requests.Response: Automation document that was requested
        """
        return self.client.call(method="GET", url=f"{self.client.url}/automation_catalog/automations/{automation_id}")

    def get_automations(self, query_parameters: Dict[str, Any]) -> "requests.Response":
        """
        Gets all known automations returned in alphabetical order
        https://apidocs.itential.com/2020.2/api/app-automation_catalog/getAutomations/

        :param query_parameters: < Undocumented >
        :return: requests.Response: List of all automation documents
        """
        params = {"queryParameters": query_parameters}
        return self.client.call(method="GET", url=f"{self.client.url}/automation_catalog/automations", params=params)

    def import_automations(
        self, automation_jsons: List[Dict[str, Any]], options: Dict[str, Any]
    ) -> "requests.Response":
        """
        Insert automation documents into the automation collection from a user supplied JSON document.
        https://apidocs.itential.com/2020.2/api/app-automation_catalog/importAutomations/

        :param automation_jsons: List of json representations of automation catalogs
        :param options:
        :return: requests.Response: Status of automation import operation
        """
        body = {"automations": automation_jsons, "options": options}
        return self.client.call(
            method="POST", url=f"{self.client.url}/automation_catalog/automations/import", json=body
        )

    def migrate_agenda_jobs(self, agenda_jobs: List[str]) -> "requests.Response":
        """
        Takes an existing Agenda Job data structure and converts it to an Automation
        https://apidocs.itential.com/2020.2/api/app-automation_catalog/migrateAgendaJobs/

        :param agenda_jobs: List of Unique ids automations
        :return: requests.Response: The result of the migration process
        """
        body = {"agendaJobs": agenda_jobs}
        return self.client.call(
            method="POST", url=f"{self.client.url}/automation_catalog/automations/migration", json=body
        )

    def run_automation(self, automation_id: str, options: Dict[str, Any]) -> "requests.Response":
        """
        Single run of an automation outside its scheduled runs, Requires a workflow to be attached to the automation.
        https://apidocs.itential.com/2020.2/api/app-automation_catalog/runAutomation/

        :param automation_id: Unique id of the automation
        :param options: Workflow based properties (Mostly undocumented)
        :return: requests.Response: {"status": "str", "message": {}, "workflowResponse": {}}
        """
        body = {"options": options}
        return self.client.call(
            method="POST", url=f"{self.client.url}/automation_catalog/automations/{automation_id}/run", json=body
        )

    def update_automation(self, automation_id: str, options: Dict[str, Any]) -> "requests.Response":
        """
        Updates an automation's attributes (including scheduling data).
        https://apidocs.itential.com/2020.2/api/app-automation_catalog/updateAutomation/

        :param automation_id: Unique id of the automation
        :param options: Object containing the fields to be updated
            ex: {"options": {
                    "workflowId": "8e3695fe-c5bf-4286-ae83-186b3fea1c1a",
                    "formId": "74cd8ca4367d4a9617c5c849",
                    "gbac": {
                      "write": [
                        "c47584c0cdb569d258a1e48c",
                        "f8ff16a4d36a61468b6ed5bc"
                      ],
                      "read": [
                        "2f829cfa07d897e682212871",
                        "2cd984705c011c5172458ac4"
                      ]
                    },
                    "nextRunAt": "2019-11-25T22:51:39.201Z",
                    "repeatInterval": null
                  }
                }
        :return: requests.Response: Updated document of requested automation
        """
        body = {"options": options}
        return self.client.call(
            method="PUT", url=f"{self.client.url}/automation_catalog/automations/{automation_id}", json=body
        )
