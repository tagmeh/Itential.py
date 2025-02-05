from src.base.models.custom_base import CustomBaseModel


class TemplateModel(CustomBaseModel):
    name: str | None
    id: str | None
    type: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}) - {self.type}"
