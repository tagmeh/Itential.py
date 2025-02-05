from abc import ABC, abstractmethod
from pathlib import Path


class ScriptsAsset(ABC):
    @abstractmethod
    def import_repo(self, repo_path: str | Path, path_to_assets: str = "resources/itential/") -> None: ...

    @abstractmethod
    def scan_for_disallowed_names(self) -> None: ...
