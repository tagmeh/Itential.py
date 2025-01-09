from pydantic import BaseModel

from src.base.itential import Itential


class CustomBaseModel(BaseModel):
    itential_instance: Itential

    class Config:
        arbitrary_types_allowed = True
