# Problem 1: Blast Radius

Robinhood's market-data platform is organized as a binary tree of services.
Each service has a unique integer ID. A parent service fans data out to at
most two downstream services, and every service also keeps a heartbeat
connection back to its parent — so an incident can spread in **both**
directions along an edge.

This morning, the service `alarm` started throwing errors. The incident
response team wants to page every service that is exactly `k` network hops
away from the alarming service, since those are the ones about to be hit
next. A hop is one edge, whether it goes to a child or up to the parent.

Given the root of the service tree, a reference to the alarming service node
`alarm` (a node inside the tree, not just an ID), and an integer `k`, return
the IDs of all services exactly `k` hops away from `alarm`. Return them in
any order.

## Reference

```python
class ServiceNode:
    def __init__(self, service_id: int, left=None, right=None):
        self.service_id = service_id
        self.left = left
        self.right = right
```

## Examples

### Example 1

```text
Input:
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4

alarm = the node with ID 5
k = 2

Output: [7, 4, 1]

Explanation:
The services 7 and 4 are two hops below service 5. Service 1 is two hops
away going up through the root: 5 -> 3 -> 1.
```

### Example 2

```text
Input:
        1
       /
      2

alarm = the node with ID 2
k = 1

Output: [1]
```

### Example 3

```text
Input:
        1

alarm = the node with ID 1
k = 3

Output: []
```

## Constraints

```text
1 <= number of services <= 500
0 <= service_id <= 500, all IDs unique
0 <= k <= 1000
alarm is a node that exists in the tree
```

## Follow-up

The incident was never contained. Postmortem review showed that once a
service starts erroring, its parent and children start erroring exactly
**one minute** later, and the failure cascades outward minute by minute
until the entire platform is down.

The SRE team wants to know how much time they actually had: return the
number of minutes until **every** service in the tree is erroring. One
twist — this time you are given only the integer ID of the alarming
service, not a reference to its node.

Can you compute the answer in a **single** traversal of the tree, without
building any graph or adjacency structure?

## Source

- [LeetCode 863](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
- Follow-up: [LeetCode 2385](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/)
