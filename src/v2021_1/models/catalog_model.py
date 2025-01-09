from datetime import datetime

from src import ItentialVersion
from src.base.models.catalog import CatalogModel


class CatalogModel2021_1(CatalogModel):
    """ """

    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}

    _version: ItentialVersion = ItentialVersion.V2021_1
