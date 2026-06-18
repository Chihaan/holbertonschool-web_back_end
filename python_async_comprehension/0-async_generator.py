#!/usr/bin/env python3
"""Module that defines an asynchronous generator of random numbers."""

import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random numbers between 0 and 10, one per second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0.0, 10.0)
