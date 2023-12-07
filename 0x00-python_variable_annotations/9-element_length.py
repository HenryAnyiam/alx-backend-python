#!/usr/bin/env python3
"""
Function with Duck Type Annotation Example
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a generator in an iterator"""
    return [(i, len(i)) for i in lst]
