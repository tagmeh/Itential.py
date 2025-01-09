from abc import abstractmethod, ABC
from typing import Any, overload, Literal


class WorkflowAsset(ABC):
    @abstractmethod
    def retrieve(self, *args, **kwargs): ...

    @abstractmethod
    def retrieve_lean(self, workflow_name: str, include: list[str] = None, exclude: list[str] = None): ...

    @abstractmethod
    def search(self, *args, **kwargs) -> list: ...

    @abstractmethod
    def download(self, workflow_name: str): ...

    @abstractmethod
    def export(self, workflow_name: str): ...

    @abstractmethod
    def upload(self, workflow, canvas_version: Literal[1, 2] = 1) -> dict | str: ...

    @abstractmethod
    def delete(self, workflow) -> str: ...
