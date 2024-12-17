import logging
from enum import Enum

logging.basicConfig(level=logging.WARNING)
log = logging.getLogger(__name__)


class SupportedVersion(Enum):
    V2021_1 = "2021.1"
    V2023_1 = "2023.1"