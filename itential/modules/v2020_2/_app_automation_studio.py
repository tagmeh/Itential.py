"""
Link to Itential Docs: https://docs.itential.com/2020.2/api/app-automation_studio/

Implemented  Doc String  Tests
    [x]         [x]       [ ]   createAutomation
    [x]         [x]       [ ]   createTemplate
    [x]         [x]       [ ]   deleteTemplate
    [x]         [x]       [ ]   getMethodOptions
    [x]         [x]       [ ]   getTemplate
    [x]         [x]       [ ]   getTemplates
    [x]         [x]       [ ]   importAutomations
    [x]         [x]       [ ]   importTemplates
    [x]         [x]       [ ]   runTransformation
    [x]         [x]       [ ]   updateAutomation
    [x]         [x]       [ ]   updateTemplate
"""
from typing import TYPE_CHECKING, List, Dict, Any

if TYPE_CHECKING:
    from itential.core import Itential
    import requests


class AppAutomationStudio:
    """https://docs.itential.com/2020.2/api/app-automation_studio/createAutomation/"""

    @staticmethod
    def create_automation(client: "Itential", automation_json: Dict[str, Any]) -> "requests.Response":
        """
        Creates a new automation document.
        https://docs.itential.com/2020.2/api/app-automation_studio/createAutomation/
        :param client: Itential state object
        :param automation_json: json representation of the Automation to create
        :return: requests.Response: Created automation and associated edit URI
        """
        body = {"automation": automation_json}
        return client.call(method="POST", url=f"{client.url}/automation-studio/automations", json=body)

    @staticmethod
    def create_template(client: "Itential", template_json: Dict[str, Any]) -> "requests.Response":
        """
        Creates a new template document.
        https://docs.itential.com/2020.2/api/app-automation_studio/createTemplate/
        :param client: Itential state object
        :param template_json: json representation of the Template to create
        :return: requests.Response: Created template and associated edit URI.
        """
        body = {"template": template_json}
        return client.call(method="POST", url=f"{client.url}/automation-studio/templates", json=body)

    @staticmethod
    def delete_template(client: "Itential", template_id: str) -> "requests.Response":
        """
        Deletes a template document.
        https://docs.itential.com/2020.2/api/app-automation_studio/deleteTemplate/
        :param client: Itential state object
        :param template_id: Unique template ID
        :return: requests.Response:
        """
        return client.call(method="DELETE", url=f"{client.url}/automation-studio/templates/{template_id}")

    @staticmethod
    def get_method_options(client: "Itential") -> "requests.Response":
        """
        Get all available rest calls in IAP.
        https://docs.itential.com/2020.2/api/app-automation_studio/getMethodOptions/
        :param client: Itential state object
        :return: requests.Response: List of all rest calls available in the system.
        """
        return client.call(method="GET", url=f"{client.url}/automation-studio/json-forms/method-options")

    @staticmethod
    def get_template(client: "Itential", template_id: str, query_parameters: Dict[str, Any]) -> "requests.Response":
        """
        Gets a single template document.
        https://docs.itential.com/2020.2/api/app-automation_studio/getTemplate/
        :param client: Itential state object
        :param template_id: ObjectId specifying a template entity.
        :param query_parameters: Optional parameters for projecting fields in the template document.
            (example in DOM only)
        :return: requests.Response:
        """
        params = {"queryParameters": query_parameters}
        return client.call(method="GET", url=f"{client.url}/automation-studio/templates/{template_id}", params=params)

    @staticmethod
    def get_templates(client: "Itential", query_parameters: Dict[str, Any]) -> "requests.Response":
        """
        Gets a page of template documents.
        https://docs.itential.com/2020.2/api/app-automation_studio/getTemplates/
        :param client: Itential state object
        :param query_parameters: Parameters for filtering, paginating, projecting, and sorting template documents.
            (example in DOM only)
        :return: requests.Response:
        """
        params = {"queryParameters": query_parameters}
        return client.call(method="GET", url=f"{client.url}/automation-studio/templates", params=params)

    @staticmethod
    def import_automations(client: "Itential", automation_list: List[Dict[str, Any]]) -> "requests.Response":
        """
        Imports a new automation document.
        https://docs.itential.com/2020.2/api/app-automation_studio/importAutomations/
        :param client: Itential state object
        :param automation_list: List of automation json representations.
        :return: requests.Response: Results from each individual import operation.
        """
        body = {"automations": automation_list}
        return client.call(method="POST", url=f"{client.url}/automation-studio/automations/import", json=body)

    @staticmethod
    def import_templates(client: "Itential", template_list: List[Dict[str, Any]]) -> "requests.Response":
        """
        Imports a new template document.
        https://docs.itential.com/2020.2/api/app-automation_studio/importTemplates/
        :param client: Itential state object
        :param template_list: List of template json representations.
        :return: requests.Response: Results from each individual import operation.
        """
        body = {"templates": template_list}
        return client.call(method="POST", url=f"{client.url}/automation-studio/templates/import", json=body)

    @staticmethod
    def run_transformation(
        client: "Itential", transformation_id: str, transformation_data: Dict[str, Any]
    ) -> "requests.Response":
        """
        Transforms data using JST transformation document.
        https://docs.itential.com/2020.2/api/app-automation_studio/runTransformation/
        :param client: Itential state object
        :param transformation_data: Transformation json representation
        :param transformation_id: Unique transformation ID
        :return: requests.Response: Transformed data.
        """
        body = {"data": transformation_data}
        return client.call(
            method="POST",
            url=f"{client.url}/automation-studio/json-forms/runTransformation/{transformation_id}",
            json=body,
        )

    @staticmethod
    def update_automation(
        client: "Itential", automation_id: str, automation_update: Dict[str, Any]
    ) -> "requests.Response":
        """
        Replaces a automation document.
        https://docs.itential.com/2020.2/api/app-automation_studio/updateAutomation/
        :param client: Itential state object
        :param automation_id: Unique automation ID
        :param automation_update: Complete automation definition/json representation to replace the
            existing automation document with.
        :return: requests.Response:
        """
        body = {"update": automation_update}
        return client.call(method="PUT", url=f"{client.url}/automation-studio/automations/{automation_id}", json=body)

    @staticmethod
    def update_template(client: "Itential", template_id: str, template_update: Dict[str, Any]) -> "requests.Response":
        """
        Replaces a template document.
        https://docs.itential.com/2020.2/api/app-automation_studio/updateTemplate/
        :param client: Itential state object
        :param template_id: Unique template ID
        :param template_update: Complete template definition to replace the existing template document with.
            May not contain fields '_id', 'created', 'createdBy', 'lastUpdated', or 'lastUpdatedBy'.
        :return: requests.Response:
        """
        body = {"update": template_update}
        return client.call(method="PUT", url=f"{client.url}/automation-studio/templates/{template_id}", json=body)
