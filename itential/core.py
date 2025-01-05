import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, overload, Literal

from itential.src.iap_versions.base import Job, Workflow
from itential.src.versions import ItentialVersion

log = logging.getLogger(__name__)


class WorkflowAssetBase(ABC):
    @abstractmethod
    @overload
    def retrieve(self, workflow_name: str, expand: list[str] = None) -> Workflow: ...

    @abstractmethod
    @overload
    def retrieve(self, query: dict[str, Any], expand: list[str] = None, **kwargs) -> Workflow: ...

    @abstractmethod
    @overload
    def retrieve(self, job: Job, expand: list[str] = None, **kwargs) -> Workflow: ...

    @abstractmethod
    @overload
    def retrieve(self, job_id: int, expand: list[str] = None, **kwargs): ...

    @abstractmethod
    def retrieve(self, **kwargs) -> Workflow | None: ...

    @abstractmethod
    def retrieve_lean(
        self, workflow_name: str, include: list[str] = None, exclude: list[str] = None
    ) -> Workflow | None: ...

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
    ) -> list[Workflow]: ...

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
    ) -> list[Workflow]: ...

    @abstractmethod
    def search(self, **kwargs) -> list[Workflow]: ...

    @abstractmethod
    def download(self, workflow_name: str) -> Workflow: ...

    @abstractmethod
    def export(self, workflow_name: str) -> Workflow: ...

    @abstractmethod
    def upload(self, workflow: dict | Workflow, canvas_version: Literal[1, 2] = 1) -> dict | str: ...

    @abstractmethod
    def delete(self, workflow: str | Workflow) -> str: ...


class JobAssetBase(ABC):
    @abstractmethod
    def retrieve(self, job_id: str) -> Job: ...

    @abstractmethod
    def retrieve_lean(self, job_id: str, include: list[str] = None, exclude: list[str] = None, **kwargs) -> Job: ...

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
    ) -> list[Job]: ...

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
    ) -> list[Job]: ...

    @abstractmethod
    def search(self, **kwargs) -> list[Job]: ...

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
    ) -> list[Job]: ...

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
    ) -> list[Job]: ...

    @abstractmethod
    def search_lean(self, **kwargs) -> list[Job]: ...

    @abstractmethod
    def output(self, job: Job | str) -> Job: ...


class Scripts(ABC):
    @abstractmethod
    def import_repo(self, repo_path: str | Path, path_to_assets: str = "resources/itential/") -> None: ...

    @abstractmethod
    def scan_for_disallowed_names(self) -> None: ...


class Itential(ABC):
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
