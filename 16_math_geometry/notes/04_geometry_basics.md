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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
