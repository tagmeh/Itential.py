from abc import abstractmethod, ABC
from typing import Any, overload, Literal


class JobAssetBase(ABC):
    @abstractmethod
    def retrieve(self, job_id: str): ...

    @abstractmethod
    def retrieve_lean(self, job_id: str, include: list[str] = None, exclude: list[str] = None, **kwargs): ...

    @abstractmethod
    @overload
    def search(
        self,
        workflow_name: str,
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
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
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
        fields: dict[str, Literal[0, 1]] = None,
    ) -> list: ...

    @abstractmethod
    def search(self, **kwargs) -> list: ...

    @abstractmethod
    @overload
    def search_lean(
        self,
        workflow_name: str,
        include: list[str] = None,
        exclude: list[str] = None,
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
    ) -> list: ...

    @abstractmethod
    @overload
    def search_lean(
        self,
        query: dict[str, Any],
        include: list[str] = None,
        exclude: list[str] = None,
        get_all: bool = False,
        max_amt: int = 0,
        expand: list[str] = None,
        limit: int = 100,
        skip: int = 0,
        sort: dict[str, Literal[1, -1]] = None,
    ) -> list: ...

    @abstractmethod
    def search_lean(self, **kwargs) -> list: ...

    @abstractmethod
    def output(self, job): ...