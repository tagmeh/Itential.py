import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Literal, overload

from itential.src.versions import ItentialVersion

log = logging.getLogger(__name__)


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
    def retrieve_lean(self, workflow_name: str, include: list[str] = None, exclude: list[str] = None): ...

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


class Scripts(ABC):
    @abstractmethod
    def import_repo(self, repo_path: str | Path, path_to_assets: str = "resources/itential/") -> None: ...

    @abstractmethod
    def scan_for_disallowed_names(self) -> None: ...


class Itential:
    _version_map: dict[ItentialVersion, str] = {
        ItentialVersion.V2021_1: "itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1",
        ItentialVersion.V2023_1: "itential.src.iap_versions.v2023_1.itential2023_1.Itential2023_1",
    }

    workflow = WorkflowAssetBase
    job = JobAssetBase
    scripts = Scripts

    @classmethod
    def create(
        cls,
        version: ItentialVersion,
        username: str = "admin@pronghorn",
        password: str = "admin",
        url: str = "http://localhost:3000",
    ) -> type["Itential"]:
        if cls.__name__ != "Itential":
            raise NotImplementedError(".create() is not available from the subclass.")

        log.debug(f"Creating version-specific Itential instance with version: {version.value}")
        module_path, class_name = Itential._version_map[version].rsplit(".", 1)
        log.debug(f"Preparing to import '{class_name}' from '{module_path}'")

        module = __import__(module_path, fromlist=[class_name])

        log.debug(f"Imported '{class_name}'")
        versioned_class = getattr(module, class_name)
        return versioned_class(username=username, password=password, url=url)
