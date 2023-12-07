#!/usr/bin/env python3
"""
Annotated Function with Complex Variable Annotation Example
"""


from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """adds a list and returns their sum"""
    return reduce((lambda a, b: a + b), input_list)
