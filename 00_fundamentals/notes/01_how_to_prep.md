# How to Prepare

Technical interview preparation is the process of turning a new idea into
something you can recognize, code, and explain without notes. Solving a large
number of random problems can feel productive, but it gives weak feedback: when
you get stuck, you cannot tell whether you missed the underlying idea or simply
had not learned it yet.

The shortest useful loop is:

```text
learn one pattern -> solve focused problems -> record the miss -> re-solve cold
```

A **pattern** is a reusable way to organize a solution, such as keeping a set of
values already seen or moving two indices through an array. You will learn each
pattern in the notes before the problem set asks you to recognize it.

## Use the Book in Order

Each numbered module has one job. Its notes teach the idea, and its problem set
turns that idea into recall. Work through a module like this:

1. Read one note and explain its main idea in your own words.
2. Type the important code yourself instead of copying it.
3. Solve the matching problem-set section in order.
4. Record why you got stuck or why your first solution failed.
5. Re-solve misses on a later day without the note or solution open.

The first few problems are **focused practice**: you know which module you are
in, so recognizing the pattern is deliberately easier. After several modules,
add **mixed practice**, where the topic label is hidden. That is when you learn
to choose a pattern instead of merely applying the one you were told to use.

Do not start with company lists. A company list changes which patterns you
practice more often; it does not replace learning those patterns. Build core
coverage first, then use mixed and company-specific sets to aim your review.

## A Miss Is Useful Only When It Is Specific

"I got confused" gives your future self nothing to fix. A useful review names
the decision that went wrong:

```text
Problem: shortest path through an unweighted grid
Miss: used depth-first search and had no guarantee of finding the shortest path
Correction: breadth-first search processes positions one distance layer at a time
Re-solve: Friday, without notes
```

Keep this record short. You are not writing a second solution. You are storing
the clue that should change your next attempt.

Classify each attempt honestly:

- A **cold solve** means you derived and coded the solution without seeing a
  hint, explanation, or old code.
- If you needed a hint or solution, the problem needs review even if you later
  typed correct code.
- A problem is **mastered** only after a cold re-solve on a later day. Immediate
  recall after reading a solution mostly measures short-term memory.

When you review, cover the solution and start from an empty editor. If you only
read your old code, you are practicing recognition, while the interview asks for
recall.

## Spend Time Where the Failure Is

Use the failure to choose the next kind of practice:

| What happens                                        | What it usually means                      | Next action                                             |
| --------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------- |
| You do not know how to begin                        | The pattern is not understood yet          | Reread the relevant note and do focused problems        |
| You can explain the idea but cannot finish the code | The implementation is not automatic yet    | Type the core shape, then solve another focused problem |
| You solve by module but not from a random list      | Recognition is weak                        | Add mixed problems without topic labels                 |
| Your code is nearly right but fails edge cases      | Testing and state tracking are weak        | Trace small inputs by hand before submitting            |
| You solve silently but struggle in mocks            | The live-coding conversation is unfamiliar | Narrate normal practice out loud                        |

This is more useful than a fixed daily quota. Two carefully reviewed problems
can repair a weakness that ten unchecked submissions leave untouched.

## Add Time Pressure Gradually

An **online assessment (OA)** is usually a timed set that rewards correct code
and quick pattern recognition. A live interview also evaluates how you clarify,
reason, test, and respond to hints. Do not train both formats from the first day.

Use three stages:

1. Learn without a timer. Stop to understand every decision.
2. Solve focused and mixed problems with a generous target time.
3. Add timed sets and mock interviews once the common implementations no longer
   consume all your attention.

During an OA, scan the whole set, take the most reliable points first, and move
on when one problem is consuming the rest of the assessment. During a live
interview, keep the interviewer with you. Twenty silent minutes followed by code
is weaker evidence than a clear approach, a stated tradeoff, and steady progress.

The next four notes teach the Python, complexity language, operation costs, and
conversation that every later module assumes.

## A Sustainable Review Rhythm

You do not need an elaborate calendar. Every study block should contain at least
one of these:

- **Learn:** read a new note and type its core code.
- **Practice:** solve problems from that note's module.
- **Review:** inspect one miss and write the exact correction.
- **Recall:** re-solve an older miss cold.
- **Perform:** solve a mixed problem or run a mock out loud.

New material and recall should both appear in a normal week. If you only learn
new topics, older ones decay. If you only repeat comfortable topics, your
coverage stops growing.

## Summary

- Preparation turns a pattern into something you can recognize, code, test, and
  explain without notes; raw problem count is not the goal.
- The shortest useful loop is to learn one pattern, solve focused problems,
  record the exact miss, and re-solve it cold on a later day.
- Notes teach, module problem sets build focused recall, mixed sets train pattern
  choice, and mocks train the full live-coding performance.
- A hint-assisted solve still needs review, because understanding a revealed
  answer is different from deriving it from an empty editor.
- Time pressure belongs after the common ideas and implementations are stable;
  otherwise the timer only rehearses getting stuck.

## Preparation Checklist

```text
Can I explain the current pattern without looking at the note?
Did I type the important code myself?
Did I record the exact reason for each miss?
Did I schedule a cold re-solve on a later day?
Am I mixing older topics after focused practice?
Am I practicing some solutions out loud?
Does my next study block target the failure I am actually having?
```
