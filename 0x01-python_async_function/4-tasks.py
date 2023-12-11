#!/usr/bin/python3
"""alter an async function"""


import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random amunt of time and return time"""
    time: float = uniform(0, max_delay)
    await asyncio.sleep(time)
    return time


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return an async task"""
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """create and call an async task"""
    task = asyncio.gather(*(task_wait_random(max_delay) for i in range(n)))
    result = await task
    return sorted(result)
