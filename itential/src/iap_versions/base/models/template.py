from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from itential import Itential


class Template(BaseModel):
    _itential: Optional["Itential"] = None  # Itential state instance.
    name: str | None
    id: str | None
    type: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}) - {self.type}"
