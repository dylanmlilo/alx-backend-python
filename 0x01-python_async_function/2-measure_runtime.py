#!/usr/bin/env python3
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): The maximum delay in seconds for wait_n.

    Returns:
        float: Average time taken per call.
    """
    start_time = time.time()
    for _ in range(n):
        asyncio.run(wait_n(1, max_delay))
    total_time = time.time() - start_time
    return total_time / n
