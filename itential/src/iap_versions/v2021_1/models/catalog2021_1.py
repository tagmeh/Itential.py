from datetime import datetime

from itential.src.iap_versions.base import Catalog
from itential.src.versions import ItentialVersion


class Catalog2021_1(Catalog):
    """ """

    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"}

    _version: ItentialVersion = ItentialVersion.V2021_1
