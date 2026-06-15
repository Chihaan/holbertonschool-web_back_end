#!/usr/bin/env python3
"""Module that runs multiple wait_random coroutines concurrently."""

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn wait_random n times and return the list of delays."""
    final_list = []
    wait_random = __import__("0-basic_async_syntax").wait_random
    arrival_list = [wait_random(max_delay) for _ in range(n)]
    for arrivals in asyncio.as_completed(arrival_list):
        result = await arrivals
        final_list.append(result)
    return final_list
