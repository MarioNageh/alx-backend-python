#!/usr/bin/env python3
"""
    4-tasks.py module
"""
import asyncio

from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n
    @n: times to call task_wait_random
    @max_delay: max delay of task_wait_random
    Return: list of all delays
    """

    dly: List[asyncio.Future[float]] = []
    for _ in range(n):
        dly.append(task_wait_random(max_delay))
    res: List[float] = []
    for delay in asyncio.as_completed(dly):
        res.append(await delay)
    return res
