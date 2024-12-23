from functools import wraps
from typing import TypeVar

funcT = TypeVar("funcT")


def inject_itential_instance(func: funcT) -> funcT:
    """
    Injects the 'itential' instance into the returned asset object.
    This allows the asset instance to make further calls to the Itential platform.
    """

    @wraps(func)
    def wrapper(itential, *args, **kwargs):
        result = func(itential, *args, **kwargs)

        # This is probably an error.
        # Todo: This section will need updating when the standard error handler is created.
        if isinstance(result, (str, dict)):
            return result

        if isinstance(result, list):
            for item in result:
                item._itential = itential
        else:
            result._itential = itential

        return result

    return wrapper
