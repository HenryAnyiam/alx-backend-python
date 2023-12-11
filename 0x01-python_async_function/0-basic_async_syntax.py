#!/usr/bin/env python3
"""implement an async function"""

import asyncio
from typing import Union
import random


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    """wait for a random amunt of time and return time"""
    time: Union[int, float] = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
