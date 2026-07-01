class UnionFind:
    # Shared disjoint set union with path compression and union by size.

    def __init__(self, n: int) -> None:
        pass

    def find(self, x: int) -> int:
        pass

    def union(self, a: int, b: int) -> bool:
        pass


def min_cost_connect_points(points: list[list[int]]) -> int:
    # Problem 8: Min Cost To Connect All Points
    # Key idea: Prim's algorithm growing a tree from a min heap of frontier edges.
    # Time:
    # Space:

    pass


def min_cost_connecting_cities(n: int, connections: list[list[int]]) -> int:
    # Problem 9: Connecting Cities With Minimum Cost
    # Key idea: Kruskal's algorithm — sort edges, union find skips cycle-forming edges.
    # Time:
    # Space:

    pass


def min_cost_to_supply_water(
    n: int, wells: list[int], pipes: list[list[int]]
) -> int:
    # Problem 10: Optimize Water Distribution In A Village
    # Key idea: treat each well as an edge from a virtual node 0, then run Kruskal's/Prim's.
    # Time:
    # Space:

    pass
