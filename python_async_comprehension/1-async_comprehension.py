#!/usr/bin/env python3
"""Module that collects random numbers using an async comprehension."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect ten random numbers from async_generator and return them."""
    numbers = [i async for i in async_generator()]
    return numbers
