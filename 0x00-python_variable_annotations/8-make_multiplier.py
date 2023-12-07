#!/usr/bin/env python3
"""
Annotated Function with Complex Variable Annotation Example
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    return (lambda x: x * multiplier)
