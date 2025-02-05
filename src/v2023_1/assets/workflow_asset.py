def get_workflow(itential, workflow_name: str) -> models.Workflow2023_1:
    """Query for a single workflow. Contains platform-aware variables like "_id" and "errors"."""
    payload = {
        "options": {
            "expand": "created_by,last_updated_by",
            # clean up and limit the amount of data returned. Expanding the user object seems to do a nested expand.
            "exclude": ",".join(
                [
                    "created_by.assignedRoles",
                    "created_by._meta",
                    "created_by.memberOf",
                    "last_updated_by.assignedRoles",
                    "last_updated_by.memberOf",
                    "last_updated_by._meta",
                ]
            ),
            "equals": {"name": workflow_name},
        }
    }
    response = itential.call(method="GET", endpoint="/automation-studio/workflows", json=payload)
    if response.ok:
        response_json = response.json()
        if response_json["total"] == 0:
            raise ValueError(f"No workflows found with name: {workflow_name}")

        elif response_json["total"] > 1:
            raise ValueError(f"Multiple workflows found with name: {workflow_name}")

        elif response_json["total"] == 1:
            return models.Workflow2023_1(**response.json()["items"][0])
    else:
        return response.reason


def export_workflow(itential, workflow_name: str) -> models.ExportedWorkflow2023_1:
    """Export a single workflow."""
    payload = {"options": {"name": workflow_name, "type": "automation"}}
    response = itential.call(method="POST", endpoint="/workflow_builder/export", json=payload)
    if response.ok:
        return models.ExportedWorkflow2023_1(**response.json())
    else:
        return response.reason
