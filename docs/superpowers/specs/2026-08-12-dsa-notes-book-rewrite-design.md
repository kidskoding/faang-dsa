# DSA Notes Book Rewrite Design

## Goal

Rewrite the active notes in modules `00` through `18` into one coherent,
teaching-first book for readers who have no LeetCode experience and want to
become ready for big-tech live-coding interviews as quickly as possible.

The approved calibration note is
[`03_stacks_and_queues/notes/02_queue_and_deque.md`](../../../03_stacks_and_queues/notes/02_queue_and_deque.md).
Its depth, natural progression, conversational prose, diagrams, dry runs,
interview reasoning, worked example, and compact reference sections define the
quality bar. Its exact headings and length do not form a template.

## Scope

- Audit all 84 active note files and rewrite the 83 notes other than the queue
  calibration note wherever they do not meet the approved standard.
- Rewrite Claude-expanded drafts as well as thin skeletons. Existing expansion
  is source material, not protected final copy.
- Work in curriculum order from module `00` through module `18`, because later
  notes may assume concepts established by earlier notes.
- Preserve the two note deletions already present in the working tree unless a
  coverage audit proves their material was not absorbed elsewhere.
- Update `skills/writing-notes/SKILL.md` so future sessions retain this house
  style, including the continuous worked-example format.
- Update `skills/writing-notes/ledger.md` whenever a rewrite changes what a note
  establishes.
- Leave module READMEs, problem sets, implementations, tests, company files,
  and unrelated user changes alone unless a broken note link requires a narrowly
  scoped correction.

## Reader And Outcome

The reader is comfortable learning Python but may not know LeetCode conventions,
interview pattern names, or the hidden assumptions inside a design problem. A
finished note must let that reader:

1. Explain what the concept is in plain language.
2. Recognize the concept when a problem disguises it.
3. Derive the implementation instead of memorizing a template.
4. Code it correctly under live-interview pressure.
5. Trace the state by hand and catch the important edge case.
6. State the time and space complexity with reasons.
7. Narrate the approach clearly to an interviewer.

The notes teach each idea once. The problem sets provide repetition and speed.

## Natural Teaching Flow

Each note should read like notes written by a strong teacher, not generated API
documentation or a checklist filled in mechanically. The usual reader journey is:

1. Define the concept with a concrete instance before using its vocabulary.
2. Show the problem signals that point to it and the nearby pattern it can be
   confused with.
3. Present one useful naive or almost-correct approach whose failure leads
   directly to the real technique.
4. Derive the invariant, state, or data movement that fixes that failure.
5. Show real, typed Python and explain only the lines that carry the idea.
6. Trace a small input, including a rejected, skipped, stale, or otherwise
   discarded step.
7. Work a relevant medium problem from the module's problem set when the note
   teaches an interview technique.
8. Finish with a compact revision layer covering complexity, summary, and an
   interview checklist.

This is a flow, not a mandatory heading list. Headings should describe the topic
in front of the reader. Meta notes in modules `00` and `18` should not invent a
LeetCode worked example or algorithmic dry run when neither belongs.

## Prose And Voice

- Preserve good existing prose and the repo's conversational teaching voice.
- Use complete, direct sentences and short paragraphs. Define jargon before
  relying on it.
- Keep the reasoning connected with plain transitions such as “because,”
  “therefore,” and “which means.”
- Be beginner-friendly without re-teaching earlier chapters. Link an earlier
  concept in one sentence and continue.
- Prefer concrete state, values, indices, and consequences over abstract claims.
- Attach the reason to every non-obvious property, bound, or design choice.
- Remove repeated explanations, throat-clearing, generic interview advice, and
  academically interesting material that the problem set does not exercise.
- Do not chase a line-count target. A note is long only when distinct techniques
  or variants require the space. Repetition is never a reason for length.

## Worked Examples

A technique note should work at least one relevant medium problem end to end when
the module's problem set contains one. The whole example remains under a single
heading:

```text
## Worked Example: [Problem Name](problem URL)
```

Do not add forced `What You Are Given`, `The Approach`, `Step By Step`, `The Solution`, or `Complexity` subheadings. Instead, let the prose move naturally
through:

- the input, return value, constraints that affect the approach, and ambiguous
  behavior that should be clarified;
- the signal that identifies the technique and the reason the obvious structure
  or brute force is insufficient;
- the invariant or central idea in language a candidate could say aloud;
- a short numbered sequence when steps genuinely improve comprehension;
- self-contained Python;
- time and space complexity as concise bullets immediately after the code.

Use a short blockquote when showing the exact interview narration materially
helps. Do not surround every explanation with labels merely to satisfy a format.

## Diagrams, Traces, And Code

- Use `text` blocks for arrays, pointer positions, state logs, and dry runs.
- Use Mermaid only for shapes with real nodes and edges, such as trees, graphs,
  linked lists, partitions, and state machines.
- Keep examples small enough to trace mentally while still exercising the branch
  that makes the algorithm interesting.
- Make every Python block runnable in the repository's supported Python version,
  with imports and type hints needed to understand it.
- Verify code blocks against official-style examples and important edge cases.
  Confirm that dry-run values match the executed code.

## Module-By-Module Process

For each module, in curriculum order:

1. Read the current notes, the prerequisite ledger, and the module problem set.
2. Map each problem-set technique to the note responsible for teaching it.
3. Rewrite every note in the module from its current working-tree contents,
   preserving correct prose while removing duplication and filling teaching gaps.
4. Check vocabulary and cross-links across the whole module.
5. Update the prerequisite ledger with the concepts the rewritten notes now
   establish.
6. Execute the note code and compare each hand trace with the results.
7. Run module-relevant tests plus Markdown and link checks.
8. Review the module against the queue calibration note before moving to the
   next module.

Claude's current uncommitted note changes are intentionally in scope. Unrelated
working-tree changes remain user-owned and must not be overwritten, reformatted,
staged, or committed.

## Verification

Every rewritten module must pass these checks before the next module begins:

- **Coverage:** every technique represented in the module problem set has teaching
  behind it, and every major note section prepares the reader for a real problem.
- **Code:** Python blocks execute with representative and edge-case assertions.
- **Traces:** dry-run state and returned values match execution.
- **Complexity:** both time and auxiliary space are stated with reasons and use
  symbols that are defined locally.
- **Links:** relative links resolve to existing repository files and external
  problem links are syntactically valid.
- **Markdown:** the module passes `mdformat --check` and `git diff --check`.
- **Tests:** relevant repository tests pass when the note teaches an implementation
  represented by local code.
- **Editorial review:** the note flows naturally, assumes only earlier material,
  contains no forced worked-example subheadings, and does not repeat itself.

After module `18`, run the checks globally and audit the ledger against the final
book order.

## Completion Condition

The rewrite is complete only when all 84 active notes have been audited, every
required rewrite is applied, the ledger and writing skill reflect the final book,
all code and traces have been verified, Markdown and links pass globally, and no
unrelated working-tree changes have been altered.
