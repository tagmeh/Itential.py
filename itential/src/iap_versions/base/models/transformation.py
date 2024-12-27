from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from itential import Itential


class Transformation(BaseModel):
    _itential: Optional["Itential"] = None  # Itential state instance.
    name: str | None  # Name of the asset, NOT unique to the platform. Unique-ness based on id field.
    id: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}) - {self.id}"
