from typing import TypeVar, TYPE_CHECKING

# from itential import Itential
from itential.src.iap_versions.base.models import Job, Workflow


J = TypeVar("J", bound=Job)  # Type-hints an object that is a subclass of Job.
W = TypeVar("W", bound=Workflow)  # Type-hints an object that is a subclass of Workflow.
# I = TypeVar("I", bound=Itential)  # Type-hints they Itential state instance object.
