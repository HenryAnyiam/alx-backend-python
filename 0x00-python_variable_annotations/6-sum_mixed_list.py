#!/usr/bin/env python3
"""
Annotated Function with Complex Variable Annotation Example
"""


from typing import List, Union
from functools import reduce


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """adds a list of integers and floats"""
    return reduce((lambda a, b: a + b), mxd_lst)
