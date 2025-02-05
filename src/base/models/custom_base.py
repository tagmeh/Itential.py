from typing import Any

from pydantic import BaseModel, Field

from src.base.itential import Itential


class CustomBaseModel(BaseModel):
    # Exclude the 'itential_instance' field from the model_dump* methods. Otherwise, you'll see serializer errors.
    itential_instance: Itential = Field(exclude=True)

    class Config:
        arbitrary_types_allowed = True

    def model_dump(self, by_alias: bool = True, **kwargs: Any) -> dict[str, Any]:
        """
        Method override to always set by_alias to True since there is no Config option for it yet.
        https://github.com/pydantic/pydantic/discussions/8725
        """
        return super().model_dump(by_alias=by_alias, **kwargs)
