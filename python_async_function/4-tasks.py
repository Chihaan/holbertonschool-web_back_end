#!/usr/bin/env python3
"""Module that runs multiple task_wait_random tasks concurrently."""

import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn task_wait_random n times and return the list of delays."""
    final_list = []
    task_wait_random = __import__("3-tasks").task_wait_random
    arrival_list = [task_wait_random(max_delay) for _ in range(n)]
    for arrivals in asyncio.as_completed(arrival_list):
        result = await arrivals
        final_list.append(result)
    return final_list
