#!/usr/bin/env python3
"""run concurrent coroutines"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """runs concurrent coroutines and returns a list"""
    result: List[float] = await asyncio.gather(*(wait_random(max_delay)
                                                 for i in range(n)))
    return sorted(result)
