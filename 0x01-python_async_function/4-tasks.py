#!/usr/bin/python3
"""alter an async function"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """create and call an async task"""
    task = asyncio.gather(*(task_wait_random(max_delay) for i in range(n)))
    result = await task
    return sorted(result)
