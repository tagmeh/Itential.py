from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from itential import Itential


class Catalog(BaseModel):
    _itential: Optional["Itential"] = None
    name: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name})"
