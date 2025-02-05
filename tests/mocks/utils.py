from pathlib import Path


def concreter(abclass):
    """
    Returns a concrete class that implements all abstract methods of the abstract class.
    https://stackoverflow.com/a/9759329

    >>> import abc
    >>> class Abstract(metaclass=abc.ABCMeta):
    ...     @abc.abstractmethod
    ...     def bar(self):
    ...        return None
    >>>
    >>> c = concreter(Abstract)
    >>> c.__name__
    'dummy_concrete_Abstract'
    >>> c().bar() # doctest: +ELLIPSIS
    (<abc_utils.Abstract object at 0x...>, (), {})
    """

    if "__abstractmethods__" not in abclass.__dict__:
        return abclass
    new_dict = abclass.__dict__.copy()
    for abstractmethod in abclass.__abstractmethods__:
        # replace each abc method or property with an identity function:
        new_dict[abstractmethod] = lambda x, *args, **kw: (x, args, kw)
    # creates a new class, with the overriden ABCs:
    return type(f"dummy_concrete_{abclass.__name__}", (abclass,), new_dict)


def get_test_base_path(path: str) -> Path:
    """
    Returns the top level tests/ directory path.

    Args:
        path: Path to the file. Can use __file__ to get the current file's path.
    """
    base_path = Path(path).resolve()
    tests_index = base_path.parts.index("tests")
    return Path(*base_path.parts[: tests_index + 1])


if __name__ == "__main__":
    assert str(get_test_base_path(__file__)).endswith(
        "\\tests"
    ), f"'{get_test_base_path(__file__)}' should end with '\\tests'"
