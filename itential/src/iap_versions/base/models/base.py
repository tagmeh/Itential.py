from typing import Optional

from pydantic import BaseModel

from itential import Itential


class CustomBaseModel(BaseModel):
    itential_instance: Optional["Itential"] = None

    class Config:
        arbitrary_types_allowed = True
