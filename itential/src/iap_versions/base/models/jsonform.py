
from itential.src.iap_versions.base.models.base import CustomBaseModel


class JsonForm(CustomBaseModel):
    name: str | None  # Name of the asset, NOT unique to the platform. Unique-ness based on id field.
    id: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}) - {self.id}"
