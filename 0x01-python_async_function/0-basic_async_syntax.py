#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive)
    seconds and returns it.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The delay in seconds.
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
