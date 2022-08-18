"""
Link to Itential Docs: https://apidocs.itential.com/2020.2/api/adapter-automation_gateway/

Implemented  Doc String  Tests
    [-]         [-]       [-]   addDeviceToDeviceGroup
    [-]         [-]       [-]   applyTerraform
    [-]         [-]       [-]   connectDevice
    [-]         [-]       [-]   createDevice
    [-]         [-]       [-]   createDeviceGroup
    [-]         [-]       [-]   createDeviceRaw
    [-]         [-]       [-]   deleteDevice
    [-]         [-]       [-]   deleteDeviceFromDeviceGroup
    [-]         [-]       [-]   deleteDeviceGroup
    [-]         [-]       [-]   destroyTerraform
    [-]         [-]       [-]   dryRunPlaybook
    [-]         [-]       [-]   getCollectionModule
    [-]         [-]       [-]   getCollectionModules
    [-]         [-]       [-]   getCollectionRole
    [-]         [-]       [-]   getCollectionRoles
    [-]         [-]       [-]   getCollections
    [-]         [-]       [-]   getConfig
    [-]         [-]       [-]   getDevice
    [-]         [-]       [-]   getDeviceDetailsRaw
    [-]         [-]       [-]   getDeviceGroup
    [-]         [-]       [-]   getDeviceGroups
    [-]         [-]       [-]   getDeviceHealth
    [-]         [-]       [-]   getDeviceInfo
    [-]         [-]       [-]   getDevices
    [-]         [-]       [-]   getDevicesDetailsRaw
    [-]         [-]       [-]   getDevicesFiltered
    [-]         [-]       [-]   getModule
    [-]         [-]       [-]   getModules
    [-]         [-]       [-]   getNornirModule
    [-]         [-]       [-]   getNornirModules
    [-]         [-]       [-]   getPlaybook
    [-]         [-]       [-]   getPlaybooks
    [-]         [-]       [-]   getPronghorn
    [-]         [-]       [-]   getRole
    [-]         [-]       [-]   getRoles
    [-]         [-]       [-]   getScript
    [-]         [-]       [-]   getScripts
    [-]         [-]       [-]   getTerraform
    [-]         [-]       [-]   getTerraforms
    [-]         [-]       [-]   initTerraform
    [-]         [-]       [-]   isAlive
    [x]         [x]       [ ]   netmikoSendCommand
    [x]         [x]       [ ]   netmikoSendConfig
    [-]         [-]       [-]   planTerraform
    [-]         [-]       [-]   refreshCollections
    [-]         [-]       [-]   refreshInventory
    [-]         [-]       [-]   refreshModules
    [-]         [-]       [-]   refreshNornirModules
    [-]         [-]       [-]   refreshPlaybooks
    [-]         [-]       [-]   refreshRoles
    [-]         [-]       [-]   refreshScripts
    [-]         [-]       [-]   restoreConfig
    [-]         [-]       [-]   runCollectionModule
    [-]         [-]       [-]   runCollectionRole
    [-]         [-]       [-]   runCommand
    [-]         [-]       [-]   runModule
    [-]         [-]       [-]   runNornirModule
    [-]         [-]       [-]   runPlaybook
    [-]         [-]       [-]   runRole
    [-]         [-]       [-]   runScript
    [-]         [-]       [-]   runScriptEnv
    [-]         [-]       [-]   setConfig
    [-]         [-]       [-]   updateDevice
    [-]         [-]       [-]   updateDeviceGroup
"""
from typing import TYPE_CHECKING, Dict, List, Union

import requests

if TYPE_CHECKING:
    from itential.core import Itential


class AdapterAutomationGateway:
    """https://apidocs.itential.com/2020.2/api/adapter-automation_gateway/"""

    @staticmethod
    def netmiko_send_command(client: "Itential", host: str, commands: List[str],
                             connection_options: Dict[str, str]) -> requests.Response:
        """
        Wrapper of send_command of netmiko.

        https://apidocs.itential.com/2020.2/api/adapter-automation_gateway/netmikoSendCommand/

        :param client: The Itential state object
        :param host: Device TID/Name
        :param commands: A List of commands to run.
        :param connection_options: Connection and Authentication information.
         Keys: "device_type", "port", "username", "password".
         See Netmiko documentation for more detail.
        :return: A JSON Object containing status, code and the result
        """
        body = {
            "netmikoSendCommandParameters": {
                "host": host,
                "commands": commands,
                "connection_options": connection_options
            }
        }
        return client.call(method="POST", url=f"{client.url}/automationgateway/netmiko/send_command", json=body)

    @staticmethod
    def netmiko_send_config(client: "Itential", host: str, config_commands: List[str],
                            connection_options: Dict[str, Union[int, str]]) -> requests.Response:
        """
        Wrapper of send_config_set of netmiko.

        https://apidocs.itential.com/2020.2/api/adapter-automation_gateway/netmikoSendConfig/

        :param client: The Itential state object
        :param host: Device TID/Name
        :param config_commands: A List of config commands to run.
        :param connection_options: Connection and Authentication information.
         Keys: "device_type", "port", "username", "password".
         See Netmiko documentation for more detail.
        :return: A JSON Object containing status, code and the result
        """
        body = {
            "netmikoSendConfigParameters": {
                "host": host,
                "config_commands": config_commands,
                "connection_options": connection_options
            }
        }
        return client.call(method="POST", url=f"{client.url}/automationgateway/netmiko/send_config", json=body)
