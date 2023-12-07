#!/usr/bin/env python3
"""
Function with Duck Type Annotation Example
"""


from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
