#!/usr/bin/env python3
"""Module that creates an asyncio Task from the wait_random coroutine."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio Task running wait_random."""
    my_task = asyncio.create_task(wait_random(max_delay))
    return my_task
