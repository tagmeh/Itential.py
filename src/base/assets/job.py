from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.base import JobModel


class JobAsset(ABC):

    @abstractmethod
    def retrieve(self, job_id: str): ...

    @abstractmethod
    def retrieve_lean(self, job_id: str, include: list[str] = None, exclude: list[str] = None, **kwargs): ...

    @abstractmethod
    def search(self, *args, **kwargs) -> list: ...

    @abstractmethod
    def search_lean(self, *args, **kwargs) -> list: ...

    @abstractmethod
    def output(self, job: JobModel | str): ...
