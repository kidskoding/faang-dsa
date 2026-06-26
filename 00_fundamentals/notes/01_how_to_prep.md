# General Technical Interview Preparation

## Pattern

Top tech preparation is a training system, not just a pile of LeetCode problems.

The loop is:

```text
learn pattern -> practice focused problems -> review misses -> re-solve -> mix topics -> mock interview
```

The notes teach the patterns. The module problem sets build targeted reps. The company problem sets help with targeting. Mixed practice and mocks turn pattern knowledge into interview performance.

## Intuition

Top tech interviews usually test a combination of:

- data structures and algorithms
- implementation speed
- pattern recognition
- debugging ability
- communication
- edge-case handling
- complexity analysis
- ability to recover when stuck

Different rounds emphasize different parts.

OAs reward speed and correctness under time pressure.

Phone screens and live coding reward clear thinking, clean implementation, and communication.

Final-round technical interviews often reward consistency across multiple patterns, not just one memorized trick.

The goal is not to memorize solutions. The goal is to recognize the pattern, derive the helper shape, code cleanly, and explain the tradeoffs.

## How This Repo Should Be Used

Use each module in this order:

```text
1. Read the module README.
2. Read the notes for the pattern.
3. Implement or review the core helper/data structure file.
4. Solve the module problem set in order.
5. Run focused tests when available.
6. Write down misses.
7. Re-solve missed problems after 3-7 days.
8. Mix the topic with older topics.
```

Reading gives you the map. Solving gives you the skill. Re-solving turns the skill into recall.

## The Core Prep Loop

For every topic, repeat this loop:

```text
understand -> implement -> practice -> review -> re-solve -> mix
```

### Understand

Read the notes until you can explain the pattern without looking.

You should be able to say:

```text
This is the pattern.
This is when I use it.
This is the state or invariant.
This is the base case.
This is the complexity.
```

### Implement

Write the core technique yourself.

Examples:

- binary search template
- tree DFS helper
- BFS queue loop
- sliding window shrink loop
- heap push/pop usage
- backtracking choose/explore/unchoose
- DP state and transition

### Practice

Do focused problems from the module problem set.

At this stage, it is okay that the topic is known. You are building the muscle memory for that pattern.

### Review

After each miss, write the concrete reason.

Bad review:

```text
I got confused.
```

Good review:

```text
I used DFS for shortest path in an unweighted grid. Correct pattern was BFS because first visit gives shortest distance.
```

### Re-Solve

Re-solve misses 3-7 days later without looking.

If you cannot solve it the second time, it was not learned yet.

### Mix

After focused practice, do mixed problems without topic labels.

This is what makes the prep interview-realistic.

## Daily Prep Template

For a normal study day:

```text
30-45 min: read/review notes for one pattern
90-120 min: solve 2-4 focused problems from that module
30 min: review misses and write what went wrong
30-45 min: re-solve one old missed problem
```

For a heavier practice day:

```text
20 min: review notes for weak patterns
2-3 hours: timed problem solving
30-45 min: postmortem and re-solve one miss
```

For a lighter maintenance day:

```text
20 min: reread one note
35 min: solve one medium
15 min: write complexity and edge cases
```

## Weekly Prep Template

A strong weekly rhythm:

```text
Day 1: focused module notes + fundamentals
Day 2: focused module problem set
Day 3: harder problems from the same module
Day 4: mixed review from older modules
Day 5: company problem set practice
Day 6: mock interview or timed OA-style set
Day 7: review, re-solve misses, light notes
```

The common failure mode is doing only new problems. The review and re-solve days are what make patterns stick.

## Topic Priority

For top tech technical interviews, prioritize the core modules first:

```text
arrays and hashing
two pointers
sliding window
stack
binary search
linked lists
trees
heaps
backtracking
graphs
dynamic programming
greedy algorithms
intervals
tries
```

Then add lower-frequency or advanced topics:

```text
bit manipulation
math and geometry
union find
shortest paths
minimum spanning tree
segment tree
Fenwick tree
advanced string algorithms
```

Advanced topics are useful, but they should not come before fluency in the core patterns.

## Company Targeting

Use company problem sets after you have basic pattern coverage.

The right order is:

```text
module notes -> module problem set -> mixed practice -> company problem set
```

Company sets are not magic. They help you bias practice toward likely patterns.

Examples:

- Google-style prep should emphasize trees, graphs, DP, backtracking, binary search, heaps, and recursion clarity.
- Amazon-style prep should emphasize arrays, strings, hash maps, trees, graphs, heaps, and implementation speed.
- Meta-style prep should emphasize arrays, strings, trees, graphs, recursion, and clean medium-speed execution.

## OA Preparation

OAs reward speed, correctness, and pattern recognition.

Use this strategy:

```text
1. Scan all problems first.
2. Solve the easiest reliable problem first.
3. Avoid spending 30+ minutes stuck on one problem.
4. Write simple correct code before optimizing.
5. Test edge cases quickly.
6. Return to harder problems with remaining time.
```

Common OA edge cases:

- empty input
- one element
- duplicates
- negative numbers
- impossible target
- disconnected graph
- very large input
- off-by-one boundaries
- integer overflow in languages where it matters

## Live Coding Preparation

Live coding is not just solving. It is solving while communicating.

Use this script:

```text
First, I will clarify the input, output, and edge cases.
The brute force approach is ...
The bottleneck is ...
The better pattern is ...
I will maintain this state/invariant ...
Now I will code the base case/helper.
Let's test the sample.
Let's test edge cases.
The time complexity is ...
The space complexity is ...
```

Practice saying this out loud while coding. It will feel slower at first. That is the point.

## Phone Screen Preparation

For phone screens, the goal is to solve one or two medium problems cleanly.

You need to show:

- clear approach
- correct code
- reasonable speed
- edge-case awareness
- complexity analysis
- ability to accept hints and adjust

Do not silently code for 20 minutes. Keep the interviewer with you.

## Mock Interview Preparation

Do mocks after you have enough focused reps that the basics do not collapse.

A useful mock should include:

```text
5 min: problem clarification and brute force
25-35 min: coding and testing
5-10 min: complexity, cleanup, follow-ups
10 min: review after the mock
```

The post-mock review matters as much as the mock.

## How To Know A Problem Is Done

A problem is done only when you can:

```text
explain the pattern
write the base case
write the helper shape
code it without looking
test edge cases
explain time and space
re-solve it days later
```

If you needed heavy hints, mark it as a miss and re-solve it later.

## Stuck Protocol

When stuck, follow this sequence:

```text
1. Restate the problem in your own words.
2. Write the brute force approach.
3. Identify the bottleneck.
4. Ask what pattern removes that bottleneck.
5. Define the state, invariant, or helper return value.
6. Write the smallest base case.
7. Test on a tiny example.
```

Pattern signals:

```text
repeated lookup -> hashing
sorted array -> binary search or two pointers
contiguous subarray/string -> sliding window or prefix sum
nearest level/shortest unweighted path -> BFS
choose/explore/unchoose -> backtracking
overlapping subproblems -> DP
repeated min/max priority -> heap
range overlap -> intervals
prefix lookup -> trie
```

## Review Loop

After every miss, write:

```text
Problem:
Missed pattern:
Bug:
Correct idea:
Re-solve date:
```

Keep the note short and concrete.

Examples:

```text
Missed pattern: Prefix sum with hash map.
Bug: Tried sliding window even though negative numbers were allowed.
Correct idea: Count previous prefix sums equal to current_sum - target.
```

```text
Missed pattern: Postorder tree DFS.
Bug: Recomputed height at every node and got O(n^2).
Correct idea: Return height and update answer in one DFS pass.
```

## Time Allocation

A good prep split:

```text
20% notes and pattern review
55% focused/timed problem solving
15% reviewing and re-solving misses
10% mixed practice or mocks
```

If you are failing problems because you do not recognize patterns, increase notes briefly.

If you understand the notes but cannot code, increase timed reps.

If you can solve by topic but fail random problems, increase mixed practice.

## Pitfalls

- Reading notes for hours without solving.
- Solving random problems before learning the pattern.
- Never re-solving missed problems.
- Looking at solutions too early.
- Memorizing exact code instead of understanding helper shapes.
- Avoiding weak topics.
- Practicing only by topic and never doing mixed sets.
- Passing tests once and never revisiting the problem.
- Doing company sets before learning the underlying modules.

## Interview Checklist

Before a serious top tech interview cycle, check:

```text
Can I solve core mediums in 25-35 minutes?
Can I explain brute force before optimizing?
Can I identify common patterns from constraints?
Can I write tree and graph helpers without freezing?
Can I write binary search boundaries cleanly?
Can I handle sliding window and prefix sum cases?
Can I define DP states for common DP problems?
Can I test edge cases without being prompted?
Can I explain time and space clearly?
Have I re-solved my misses?
Have I done mixed practice without topic labels?
Have I done at least a few mock interviews out loud?
```

If the answer is no, the fix is focused reps and review.
