import logging

from src.factory import create_itential
from src.versions import ItentialVersion

__all__ = ["create_itential", "ItentialVersion"]

console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logging.basicConfig(level=logging.DEBUG, handlers=[console_handler])
