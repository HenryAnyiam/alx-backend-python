#!/usr/bin/env python3
"""Uses List Comprehension"""


import asyncio
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    uses list comprehension to get values from an
    async generator
    """
    return [i async for i in async_generator()]
