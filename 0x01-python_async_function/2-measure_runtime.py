#!/usr/bin/env python3
""" 2. Measure the runtime

    Write a function (do not create an async function, use the regular"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n: times to call wait_random
        max_delay: max delay of wait_random
        Return: total_time / n
    """

    s: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    d: float = time.perf_counter()
    total_time: float = d - s

    return total_time / n
