#!/usr/bin/env python3
"""
Annotated Function with Complex Variable Annotation Example
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of the given args"""
    return (k, (v ** 2))
