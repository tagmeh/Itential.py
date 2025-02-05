from src.base.models.custom_base import CustomBaseModel


class JsonFormModel(CustomBaseModel):
    name: str | None  # Name of the asset, NOT unique to the platform. Unique-ness based on id field.
    id: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}) - {self.id}"
