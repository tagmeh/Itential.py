from typing import TypeVar, TYPE_CHECKING

# from itential2 import Itential
from itential2.src.iap_versions.core.models import Job, Workflow


J = TypeVar("J", bound=Job)  # Type-hints an object that is a subclass of Job.
W = TypeVar("W", bound=Workflow)  # Type-hints an object that is a subclass of Workflow.
# I = TypeVar("I", bound=Itential)  # Type-hints they Itential state instance object.
