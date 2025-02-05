from abc import ABC, abstractmethod


class UtilsAsset(ABC):
    @abstractmethod
    def version(self) -> str: ...
