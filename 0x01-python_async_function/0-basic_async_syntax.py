#!/usr/bin/env python3
"""implement an async function"""

import asyncio
from typing import Union
from random import uniform


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    """wait for a random amunt of time and return time"""
    time: Union[int, float] = uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
