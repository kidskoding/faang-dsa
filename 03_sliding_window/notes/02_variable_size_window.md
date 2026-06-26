# Variable-Size Sliding Window

## Pattern

Expand the right side and shrink the left side until the window satisfies the condition.

## Intuition

The window changes size based on validity. This works when moving left forward never needs to be undone.

## How It Works

Variable windows are common for shortest/longest subarray or substring problems.

## Template

```text
left = 0
for right in range(len(nums)):
    add nums[right]

    while window is invalid:
        remove nums[left]
        left += 1

    update answer
```

## Example

For longest substring without repeating characters, expand right and shrink left while a duplicate exists.

## Complexity

```text
Time: O(n)
Space: O(k) or O(n), depending on stored window state
```

## Pitfalls

- Using sliding window when negative numbers break monotonicity.
- Forgetting to remove left-side state before incrementing left.
- Updating longest/shortest answer at the wrong time.

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
