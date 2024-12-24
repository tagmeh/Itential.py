import logging
from abc import ABC, abstractmethod
from typing import Any, overload, Type

from itential.src.iap_versions.base import Job, Workflow
from itential.src.versions import ItentialVersion

log = logging.getLogger(__name__)


class Itential(ABC):
    _version_map: dict[ItentialVersion, str] = {
        ItentialVersion.V2021_1: "itential.src.iap_versions.v2021_1.itential2021_1.Itential2021_1",
        ItentialVersion.V2023_1: "itential.src.iap_versions.v2023_1.itential2023_1.Itential2023_1",
    }

    @classmethod
    def create(
        cls,
        version: ItentialVersion,
        username: str = "admin@pronghorn",
        password: str = "admin",
        url: str = "http://localhost:3000",
    ) -> Type["Itential"]:
        if cls.__name__ != "Itential":
            raise NotImplementedError(".create() is not available from the subclass.")

        log.debug(f"Creating version-specific Itential instance with version: {version.value}")
        module_path, class_name = Itential._version_map[version].rsplit(".", 1)
        log.debug(f"Preparing to import '{class_name}' from '{module_path}'")

        module = __import__(module_path, fromlist=[class_name])

        log.debug(f"Imported '{class_name}'")
        versioned_class = getattr(module, class_name)
        return versioned_class(username=username, password=password, url=url)

    @abstractmethod
    def get_job(self, job_id: str) -> Job: ...

    @abstractmethod
    def get_lean_job(self, job_id: str, include: list[str] = None, exclude: list[str] = None, **kwargs) -> Job: ...

    @abstractmethod
    @overload
    def get_jobs(self, workflow_name: str, get_all: bool = False, max_amt: int = 0, **kwargs) -> list[Job]: ...

    @abstractmethod
    @overload
    def get_jobs(self, query: dict[str, Any], get_all: bool = False, max_amt: int = 0, **kwargs) -> list[Job]: ...

    @abstractmethod
    def get_jobs(self, **kwargs: dict[str, Any]) -> list[Job]: ...

    @abstractmethod
    @overload
    def get_job_output(self, job: Job) -> Job: ...

    @abstractmethod
    @overload
    def get_job_output(self, job_id: str) -> Job: ...

    @abstractmethod
    def get_job_output(self, **kwargs: dict[str, Any]) -> Job: ...

    @abstractmethod
    @overload
    def get_lean_jobs(
        self,
        workflow_name: str,
        include: list[str] = None,
        exclude: list[str] = None,
        get_all: bool = False,
        max_amt: int = 0,
        **kwargs,
    ) -> list[Job]: ...

    @abstractmethod
    @overload
    def get_lean_jobs(
        self,
        query: dict[str, Any],
        include: list[str] = None,
        exclude: list[str] = None,
        get_all: bool = False,
        max_amt: int = 0,
        **kwargs,
    ) -> list[Job]: ...

    @abstractmethod
    def get_lean_jobs(self, **kwargs) -> list[Job]: ...

    @abstractmethod
    @overload
    def get_workflow(self, workflow_name: str, expand: list[str] = None) -> Workflow: ...

    @abstractmethod
    @overload
    def get_workflow(self, query: dict[str, Any], expand: list[str] = None, **kwargs) -> Workflow: ...

    @abstractmethod
    @overload
    def get_workflow(self, job: "Job", expand: list[str] = None, **kwargs) -> Workflow: ...

    @abstractmethod
    @overload
    def get_workflow(self, job_id: int, expand: list[str] = None, **kwargs): ...

    @abstractmethod
    def get_workflow(self, **kwargs: dict[str, Any]) -> Workflow: ...

    @abstractmethod
    def get_lean_workflow(
        self, workflow_name: str, include: list[str] = None, exclude: list[str] = None
    ) -> Workflow: ...

    @abstractmethod
    @overload
    def get_workflows(
        self, workflow_name: str, get_all: bool = False, max_amt: int = None, **kwargs
    ) -> list[Workflow]: ...

    @abstractmethod
    @overload
    def get_workflows(
        self, query: dict[str, Any], get_all: bool = False, max_amt: int = None, **kwargs
    ) -> list[Workflow]: ...

    @abstractmethod
    def get_workflows(self, **kwargs: dict[str, Any]) -> list[Workflow]: ...

    @abstractmethod
    def export_workflow(self, workflow_name: str) -> Workflow: ...
