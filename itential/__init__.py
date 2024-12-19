from itential.core import *
from itential.src.versions import ItentialVersion

console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logging.basicConfig(level=logging.DEBUG, handlers=[console_handler])

__all__ = ["Itential", "ItentialVersion"]
