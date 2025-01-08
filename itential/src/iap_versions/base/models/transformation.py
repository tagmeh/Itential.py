from typing import TYPE_CHECKING, Optional

from itential.src.iap_versions.base.models.base import CustomBaseModel

if TYPE_CHECKING:
    from itential import Itential


class Transformation(CustomBaseModel):
    name: str | None  # Name of the asset, NOT unique to the platform. Unique-ness based on id field.
    id: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}) - {self.id}"
