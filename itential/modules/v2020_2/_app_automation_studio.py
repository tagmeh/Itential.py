"""
Link to Itential Docs: https://apidocs.itential.com/2020.2/api/app-automation_studio/

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
    """https://apidocs.itential.com/2020.2/api/app-automation_studio/createAutomation/"""

    def __init__(self, client: "Itential"):
        self.client = client

    def create_automation(self, automation_json: Dict[str, Any]) -> "requests.Response":
        """
        Creates a new automation document.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/createAutomation/

        :param automation_json: json representation of the Automation to create
        :return: requests.Response: Created automation and associated edit URI
        """
        body = {"automation": automation_json}
        return self.client.call(method="POST", url=f"{self.client.url}/automation-studio/automations", json=body)

    def create_template(self, template_json: Dict[str, Any]) -> "requests.Response":
        """
        Creates a new template document.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/createTemplate/

        :param template_json: json representation of the Template to create
        :return: requests.Response: Created template and associated edit URI.
        """
        body = {"template": template_json}
        return self.client.call(method="POST", url=f"{self.client.url}/automation-studio/templates", json=body)

    def delete_template(self, template_id: str) -> "requests.Response":
        """
        Deletes a template document.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/deleteTemplate/

        :param template_id: Unique template ID
        :return: requests.Response:
        """
        return self.client.call(method="DELETE", url=f"{self.client.url}/automation-studio/templates/{template_id}")

    def get_method_options(self) -> "requests.Response":
        """
        Get all available rest calls in IAP.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/getMethodOptions/

        :return: requests.Response: List of all rest calls available in the system.
        """
        return self.client.call(method="GET", url=f"{self.client.url}/automation-studio/json-forms/method-options")

    def get_template(self, template_id: str, query_parameters: Dict[str, Any]) -> "requests.Response":
        """
        Gets a single template document.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/getTemplate/

        :param template_id: ObjectId specifying a template entity.
        :param query_parameters: Optional parameters for projecting fields in the template document.
            (example in DOM only)
        :return: requests.Response:
        """
        params = {"queryParameters": query_parameters}
        return self.client.call(
            method="GET", url=f"{self.client.url}/automation-studio/templates/{template_id}", params=params
        )

    def get_templates(self, query_parameters: Dict[str, Any]) -> "requests.Response":
        """
        Gets a page of template documents.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/getTemplates/

        :param query_parameters: Parameters for filtering, paginating, projecting, and sorting template documents.
            (example in DOM only)
        :return: requests.Response:
        """
        params = {"queryParameters": query_parameters}
        return self.client.call(method="GET", url=f"{self.client.url}/automation-studio/templates", params=params)

    def import_automations(self, automation_list: List[Dict[str, Any]]) -> "requests.Response":
        """
        Imports a new automation document.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/importAutomations/

        :param automation_list: List of automation json representations.
        :return: requests.Response: Results from each individual import operation.
        """
        body = {"automations": automation_list}
        return self.client.call(method="POST", url=f"{self.client.url}/automation-studio/automations/import", json=body)

    def import_templates(self, template_list: List[Dict[str, Any]]) -> "requests.Response":
        """
        Imports a new template document.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/importTemplates/

        :param template_list: List of template json representations.
        :return: requests.Response: Results from each individual import operation.
        """
        body = {"templates": template_list}
        return self.client.call(method="POST", url=f"{self.client.url}/automation-studio/templates/import", json=body)

    def run_transformation(self, transformation_id: str, transformation_data: Dict[str, Any]) -> "requests.Response":
        """
        Transforms data using JST transformation document.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/runTransformation/

        :param transformation_data: Transformation json representation
        :param transformation_id: Unique transformation ID
        :return: requests.Response: Transformed data.
        """
        body = {"data": transformation_data}
        return self.client.call(
            method="POST",
            url=f"{self.client.url}/automation-studio/json-forms/runTransformation/{transformation_id}",
            json=body,
        )

    def update_automation(self, automation_id: str, automation_update: Dict[str, Any]) -> "requests.Response":
        """
        Replaces a automation document.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/updateAutomation/

        :param automation_id: Unique automation ID
        :param automation_update: Complete automation definition/json representation to replace the
            existing automation document with.
        :return: requests.Response:
        """
        body = {"update": automation_update}
        return self.client.call(
            method="PUT", url=f"{self.client.url}/automation-studio/automations/{automation_id}", json=body
        )

    def update_template(self, template_id: str, template_update: Dict[str, Any]) -> "requests.Response":
        """
        Replaces a template document.
        https://apidocs.itential.com/2020.2/api/app-automation_studio/updateTemplate/

        :param template_id: Unique template ID
        :param template_update: Complete template definition to replace the existing template document with.
            May not contain fields '_id', 'created', 'createdBy', 'lastUpdated', or 'lastUpdatedBy'.
        :return: requests.Response:
        """
        body = {"update": template_update}
        return self.client.call(
            method="PUT", url=f"{self.client.url}/automation-studio/templates/{template_id}", json=body
        )
