# Grid BFS And Multi-Source BFS

## Pattern

Grid BFS finds shortest distance in unweighted grid movement. Multi-source BFS starts from all sources at once.

## Intuition

BFS expands in waves. The first time you reach a cell is the shortest distance from the nearest source.

## How It Works

Push all starting cells into the queue with distance 0. Then process level by level.

## Template

```text
queue = deque(all sources)
while queue:
    r, c = queue.popleft()
    for each neighbor:
        if valid and unvisited:
            mark distance
            queue.append(neighbor)
```

## Example

In rotting oranges, all rotten oranges start in the queue. Each BFS layer is one minute.

## Complexity

```text
Time: O(rows * cols)
Space: O(rows * cols)
```

## Pitfalls

- Starting BFS from one source at a time instead of all sources.
- Counting minutes incorrectly by one.
- Marking visited too late and enqueuing duplicates.

## Interview Checklist

Before coding, make sure you can answer:

```text
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
