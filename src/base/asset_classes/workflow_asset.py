from abc import abstractmethod, ABC
from typing import Any, overload, Literal


class WorkflowAssetBase(ABC):
    @abstractmethod
    @overload
    def retrieve(self, workflow_name: str, expand: list[str] = None): ...

    @abstractmethod
    @overload
    def retrieve(self, query: dict[str, Any], expand: list[str] = None, **kwargs): ...

    @abstractmethod
    @overload
    def retrieve(self, job, expand: list[str] = None, **kwargs): ...

    @abstractmethod
    @overload
    def retrieve(self, job_id: int, expand: list[str] = None, **kwargs): ...

    @abstractmethod
    def retrieve(self, **kwargs): ...

    @abstractmethod
    def retrieve_lean(
        self, workflow_name: str, include: list[str] = None, exclude: list[str] = None
    ): ...

    @abstractmethod
    @overload
    def search(
        self,
        workflow_name: str,
        get_all: bool = False,
        max_amt: int = None,
        expand: list[str] = None,
        limit: int = 1,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
        fields: dict[str, Literal[0, 1]] = None,
    ) -> list: ...

    @abstractmethod
    @overload
    def search(
        self,
        query: dict[str, Any],
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 1,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
        fields: dict[str, Literal[0, 1]] = None,
    ) -> list: ...

    @abstractmethod
    def search(self, **kwargs) -> list: ...

    @abstractmethod
    def download(self, workflow_name: str): ...

    @abstractmethod
    def export(self, workflow_name: str): ...

    @abstractmethod
    def upload(self, workflow, canvas_version: Literal[1, 2] = 1) -> dict | str: ...

    @abstractmethod
    def delete(self, workflow) -> str: ...
