"""
Link to Itential Docs: https://docs.itential.com/2020.2/api/app-automation_catalog/

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
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    import requests

    from itential.core import Itential


class AppAutomationCatalog:
    """https://docs.itential.com/2020.2/api/app-automation_catalog/"""

    @staticmethod
    def create_automation(client: "Itential", name: str, description: str) -> "requests.Response":
        """
        Creates an automation with optional description.
        An automation's root structure is based off the agenda.js library,
         with any custom data falling into the 'data' array
        https://docs.itential.com/2020.2/api/app-automation_catalog/createAutomation/
        :param client: Itential state object
        :param name: Unique name of the automation
        :param description: Short description of the automation
        :return: requests.Response: Automation document that was created by the request
        """
        body = {"name": name, "description": description}
        return client.call(method="POST", url=f"{client.url}/automation_catalog/automations", json=body)

    @staticmethod
    def delete_automations(client: "Itential", ids: List[str]) -> "requests.Response":
        """
        Deletes automations (based off an array of Ids)
        https://docs.itential.com/2020.2/api/app-automation_catalog/deleteAutomations/
        :param client: Itential state object
        :param ids: List of automation IDs
        :return: requests.Response: Object containing a property removeCount
        """
        body = {"ids": ids}
        return client.call(method="DELETE", url=f"{client.url}/automation_catalog/automations", json=body)

    @staticmethod
    def export_automations(client: "Itential", automation_id: str) -> "requests.Response":
        """
        Returns a single automation formatted for importing
        https://docs.itential.com/2020.2/api/app-automation_catalog/exportAutomation/
        :param client: Itential state object
        :param automation_id: Unique id of the automation
        :return: requests.Response: Automation document that was requested in exported format
        """
        return client.call(method="GET", url=f"{client.url}/automation_catalog/automations/{automation_id}/export")

    @staticmethod
    def get_automation_by_id(client: "Itential", automation_id: str) -> "requests.Response":
        """
        Gets an single automation by its id
        https://docs.itential.com/2020.2/api/app-automation_catalog/getAutomationById/
        :param client: Itential state object
        :param automation_id: Unique id of the automation
        :return: requests.Response: Automation document that was requested
        """
        return client.call(method="GET", url=f"{client.url}/automation_catalog/automations/{automation_id}")

    @staticmethod
    def get_automations(client: "Itential", query_parameters: Dict[str, Any]) -> "requests.Response":
        """
        Gets all known automations returned in alphabetical order
        https://docs.itential.com/2020.2/api/app-automation_catalog/getAutomations/
        :param client: Itential state object
        :param query_parameters: < Undocumented >
        :return: requests.Response: List of all automation documents
        """
        params = {"queryParameters": query_parameters}
        return client.call(method="GET", url=f"{client.url}/automation_catalog/automations", params=params)

    @staticmethod
    def import_automations(
        client: "Itential", automation_jsons: List[Dict[str, Any]], options: Dict[str, Any]
    ) -> "requests.Response":
        """
        Insert automation documents into the automation collection from a user supplied JSON document.
        https://docs.itential.com/2020.2/api/app-automation_catalog/importAutomations/
        :param client: Itential state object
        :param automation_jsons: List of json representations of automation catalogs
        :param options:
        :return: requests.Response: Status of automation import operation
        """
        body = {"automations": automation_jsons, "options": options}
        return client.call(method="POST", url=f"{client.url}/automation_catalog/automations/import", json=body)

    @staticmethod
    def migrate_agenda_jobs(client: "Itential", agenda_jobs: List[str]) -> "requests.Response":
        """
        Takes an existing Agenda Job data structure and converts it to an Automation
        https://docs.itential.com/2020.2/api/app-automation_catalog/migrateAgendaJobs/
        :param client: Itential state object
        :param agenda_jobs: List of Unique ids automations
        :return: requests.Response: The result of the migration process
        """
        body = {"agendaJobs": agenda_jobs}
        return client.call(method="POST", url=f"{client.url}/automation_catalog/automations/migration", json=body)

    @staticmethod
    def run_automation(client: "Itential", automation_id: str, options: Dict[str, Any]) -> "requests.Response":
        """
        Single run of an automation outside its scheduled runs, Requires a workflow to be attached to the automation.
        https://docs.itential.com/2020.2/api/app-automation_catalog/runAutomation/
        :param client: Itential state object
        :param automation_id: Unique id of the automation
        :param options: Workflow based properties (Mostly undocumented)
        :return: requests.Response: {"status": "str", "message": {}, "workflowResponse": {}}
        """
        body = {"options": options}
        return client.call(
            method="POST", url=f"{client.url}/automation_catalog/automations/{automation_id}/run", json=body
        )

    @staticmethod
    def update_automation(client: "Itential", automation_id: str, options: Dict[str, Any]) -> "requests.Response":
        """
        Updates an automation's attributes (including scheduling data).
        https://docs.itential.com/2020.2/api/app-automation_catalog/updateAutomation/
        :param client: Itential state object
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
        return client.call(method="PUT", url=f"{client.url}/automation_catalog/automations/{automation_id}", json=body)
