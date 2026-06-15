#!/usr/bin/env python3
"""Module that measures the runtime of the wait_n coroutine."""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Measure the average execution time of wait_n and return it."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    final_time = (end - start) / n
    return final_time
