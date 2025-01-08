from typing import TYPE_CHECKING, Optional

from itential.src.iap_versions.base.models.base import CustomBaseModel


class Template(CustomBaseModel):
    name: str | None
    id: str | None
    type: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}) - {self.type}"
