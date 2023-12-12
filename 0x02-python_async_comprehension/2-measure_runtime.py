#!/usr/bin/env python3
"""Measures time for an Async Generator"""


import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measure runtime of concurrent coroutines"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter() - start
    return end
