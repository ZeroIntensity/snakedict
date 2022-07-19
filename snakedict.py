from typing import Dict, TypeVar, Any, Callable
from typing_extensions import ParamSpec
import re
from functools import wraps

__all__ = (
    "convert",
    "auto",
)

T = TypeVar("T")
A = TypeVar("A")
P = ParamSpec("P")

FINDER_REGEX = re.compile(r"([a-z]+((\d)|([A-Z0-9][a-z0-9]+))*([A-Z])?)\Z")
CONVERTER_REGEX = re.compile(r"(?<!^)(?=[A-Z])")


def _switch_case_str(data: str) -> str:
    res = ""

    for i in data:
        res += "_" + i.lower() if i == i.upper() else i

    return res


def _switch_case(data: str) -> str:
    return CONVERTER_REGEX.sub("_", data).lower()


def convert(data: Dict[A, T], *, use_regex: bool = True) -> Dict[A, T]:
    """Convert a dictionaries keys to snake case."""
    new = data.copy()

    for i in data:
        if isinstance(i, str):
            if FINDER_REGEX.match(i):
                new_name: str = (
                    _switch_case(i) if use_regex else _switch_case_str(i)
                )  # fmt: off
                new[new_name] = new.pop(i)  # type: ignore
                # apparently mypy cant see isinstance

    return new


def auto(execute_maybe: bool = True):
    """Convert a dictionary to snake case upon returning."""

    def decorator(
        func: Callable[P, Dict[Any, T]],
    ) -> Callable[P, Dict[Any, T]]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> Dict[Any, T]:
            res = func(*args, **kwargs)

            if not isinstance(res, dict):
                if not execute_maybe:
                    raise TypeError(
                        f"{func.__name__} returned {res}, which is not a dict",
                    )
            else:
                res = convert(res)

            return res

        return inner

    return decorator
