"""
This app contains all of the methods used to modify transformations/JSTs on the server.
Link to Itential Docs: https://apidocs.itential.com/2020.2/api/app-jst/

Implemented  Doc String  Tests
    [x]         [x]       [x]   createTransformation
    [x]         [x]       [x]   deleteTransformation
    [x]         [x]       [ ]   getTransformation
    [x]         [x]       [ ]   importTransformation
    [x]         [x]       [ ]   runTransformation
    [x]         [x]       [ ]   searchTransformations
    [x]         [x]       [ ]   updateTransformation

"""
import json
from typing import TYPE_CHECKING, Dict, Any, Optional

if TYPE_CHECKING:
    from itential.core import Itential
    import requests


class AppJst:
    """https://apidocs.itential.com/2020.2/api/app-jst"""

    @staticmethod
    def create_transformation(client: "Itential", jst_obj: Dict[str, Any]) -> "requests.Response":
        """
        Creates a single transformation.
        https://apidocs.itential.com/2020.2/api/app-jst/createTransformation/ (Misleading param example and schema)
        :param client: Itential state object
        :param jst_obj: Json object representation of the JST
        :return: requests.Response
        """
        return client.call(method="POST", url=f"{client.url}/transformations", json=jst_obj)

    @staticmethod
    def delete_transformation(client: "Itential", jst_id: str) -> "requests.Response":
        """
        Deletes a single transformation from the server.
        https://apidocs.itential.com/2020.2/api/app-jst/deleteTransformation/
        :param client: Itential state object
        :param jst_id: "_id" field of the JST json. ex: 6230fd0b56192935eed3eeb8
        :return: requests.Response  200: empty string
        """
        return client.call(method="DELETE", url=f"{client.url}/transformations/{jst_id}")

    @staticmethod
    def get_transformations(client: "Itential", jst_id: str) -> "requests.Response":
        """
        Returns all transformations from the server, in full. This can return a rather large payload.
        Documentation is incorrect. Doesn't require "queryParameters". Don't have any examples of queryParameters usage.
        https://apidocs.itential.com/2021.2/api/app-jst/searchTransformations/
        :param client: Itential state object
        :param jst_id: "_id" field of the JST json. ex: 6230fd0b56192935eed3eeb8
        :return: requests.Response
        """
        return client.call(method="GET", url=rf"{client.url}/transformations/{jst_id}")

    @staticmethod
    def import_transformation(client: "Itential", jst_obj: Dict[str, Any]) -> "requests.Response":
        """
        Imports a single transformation/JST to the server. Will duplicate files if JST already exists.
        Will append a " (n)" to the end of the JST name. "n" is an incrementing integer
        https://apidocs.itential.com/2020.2/api/app-jst/importTransformation/ (Misleading param example and schema)
        :param client: Itential state object
        :param jst_obj: The json object representation of the transformation/JST
        :return: requests.Response
        """
        return client.call(method="POST", url=f"{client.url}/transformations/import", json=jst_obj)

    @staticmethod
    def run_transformation(
        client: "Itential", jst_id: str, incoming: Dict[str, Any], options: Optional[Dict[str, Any]] = None
    ) -> "requests.Response":
        """
        Runs a transformation
        https://apidocs.itential.com/2020.2/api/app-jst/runTransformation/
        :param client: Itential state object
        :param jst_id: "_id" of the JST. ex: 6143988e49bd502787711378
        :param incoming: A dict object of the input schema.
        :param options: < Unclear > This is not required to run a transformation.
        :return: requests.Response Returns the outgoing schema as a json obj
        """
        data = {"incoming": incoming, "options": options if options else {}}
        return client.call(method="POST", url=f"{client.url}/transformations/{jst_id}", json=data)

    @staticmethod
    def search_transformations(client: "Itential") -> "requests.Response":
        """
        Returns all transformations from the server, in full. This can return a rather large payload.
        Doesn't require "queryParameters". The usage found in the website DOM is not correct
        Documentation is incomplete. Requires further testing to figure this one out.
        https://apidocs.itential.com/2021.2/api/app-jst/searchTransformations/
        :param client: Itential state object
        :param query_parameters: < Unclear > Omitted the implementation at this time.
        :return: requests.Response
        """
        return client.call(method="GET", url=rf"{client.url}/transformations")

    @staticmethod
    def update_transformation(client: "Itential", jst_id: str, jst_obj: Dict[str, Any]) -> "requests.Response":
        """
        Updates/Overwrites an existing transformation/JST based on ID. Does not create a duplicate file.
        https://apidocs.itential.com/2020.2/api/app-jst/updateTransformation/  (Misleading param example and schema)
        :param client: Itential state object
        :param jst_id: "_id" field of the JST json. ex: 6230fd0b56192935eed3eeb8
        :param jst_obj: Full JST json. Does not require {"transformation": JST_json} like docs show.
        :return: requests.Response
        """
        return client.call(method="PUT", url=f"{client.url}/transformations/{jst_id}", json=jst_obj)
