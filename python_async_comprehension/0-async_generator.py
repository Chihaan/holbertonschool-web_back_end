#!/usr/bin/env python3
"""Module that defines an asynchronous generator of random numbers."""

from asyncio import sleep
from typing import AsyncGenerator, Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """Yield ten random numbers between 0 and 10, one per second."""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
