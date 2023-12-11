#!/usr/bin/env python3

import asyncio

async def coro1():
    await asyncio.sleep(1)
    return "Result from coro1"

async def coro2():
    await asyncio.sleep(2)
    return "Result from coro2"

async def main():
    tasks = [coro1(), coro2()]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        result = await task
        print("Completed:", result)

asyncio.run(main())