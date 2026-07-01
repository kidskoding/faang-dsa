# Geometry Basics

## Pattern

Geometry problems usually reduce to slopes, distances, orientation, or coordinate transforms.

## Intuition

Avoid floating point when exact integer comparison works.

## How It Works

Compare squared distances instead of distances when possible.

## Template

```text
dist2 = (x1-x2)^2 + (y1-y2)^2
slope key = reduced dy/dx
```

## Example

The closest point to origin can be ranked by squared distance.

## Complexity

```text
Often O(n log n) with sorting or heap
Space varies
```

## Pitfalls

- Using floating slopes and precision errors.
- Forgetting vertical lines.
- Not normalizing signs in slope keys.

## Interview Checklist

Before coding, make sure you can answer:

```text
Can I compare squared distances instead of taking a sqrt, and does that preserve the ordering I need?
Am I representing slope as a reduced (dy, dx) pair instead of a float, to avoid precision errors?
Have I handled vertical lines (dx = 0) separately so I don't divide by zero?
Did I normalize the sign of my slope key (e.g., always positive dx) so equivalent slopes hash the same?
Does the problem need exact orientation (cross product sign) rather than distance or slope at all?
What is the time and space complexity, and does sorting or a heap dominate it?
```
