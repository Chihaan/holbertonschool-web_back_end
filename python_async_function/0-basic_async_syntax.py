#!/usr/bin/env python3
"""Module that defines an asynchronous coroutine waiting a random delay."""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait a random delay between 0 and max_delay seconds and return it."""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
