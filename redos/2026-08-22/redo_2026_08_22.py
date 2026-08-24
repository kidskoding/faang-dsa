# Redo — 2026-08-22
#
# Second attempt at the four hashing problems that needed help on 2026-08-19.
# Write each from scratch. Do not open hashing_problems.py first.

import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # Top K Frequent Elements
    # First time: scanned the map k times, O(n*k). Aim for the bucket sort, O(n).
    # Time:
    # Space:

    map = {}
    heap = []
    for x in nums:
        map[x] = map.get(x, 0) + 1

    for k, v in map.items():
        heapq.heappush(heap, (v, k))
        if len(heap) > k:
            heapq.heappop(heap)

    return [value for _, value in heap]
