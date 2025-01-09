from src.base.models.custom_base import CustomBaseModel


class CatalogModel(CustomBaseModel):
    name: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name})"
