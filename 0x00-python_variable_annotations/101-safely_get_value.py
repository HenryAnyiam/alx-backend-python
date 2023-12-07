#!/usr/bin/env python3
"""
Function with Duck Type Annotation Example
"""


from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """return dict key or default"""
    if key in dct:
        return dct[key]
    else:
        return default
