from itential.src.iap_versions.base.models.base import CustomBaseModel


class Catalog(CustomBaseModel):
    name: str | None

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.name})"
