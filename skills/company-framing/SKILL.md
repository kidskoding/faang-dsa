---
name: company-framing
description: Use when creating mock interview problems, company OA-style questions, or disguising a LeetCode problem as a company-themed story — e.g. building a mock interview for a specific company, writing problem docs under mock-interviews/, or when the user invokes /company-framing.
---

# Company Problem Framing

Wrap a LeetCode-style problem in a company-themed narrative stem, the way real
OAs and onsites do — the candidate must recognize the pattern through the
disguise.

## Output shape (per problem doc)

A problem doc has these sections, in this order, and nothing else:

1. `# Problem N: <Themed Title>` — story title, tied to the company's domain
   (fintech for Robinhood, logistics for Amazon, etc.)
1. Story paragraphs — themed entities (services, trades, packages…), then the
   ask as a plain directive: "Return the …".
1. `## Reference` — data-structure class definition only (e.g. a themed
   `TreeNode`), present only when the input is a linked structure.
1. `## Examples` — 2–4 `### Example N` blocks with themed Input/Output;
   include at least one edge case (single node, empty result, boundary split).
   Any prose justifying an output goes **inside the same code block**, on an
   `Explanation:` line after the `Output:` line — never as a loose paragraph
   after the fence.
1. `## Constraints` — text code block, LeetCode-style bounds restated in
   themed terms.
1. `## Follow-up` — optional; a harder verbal extension.
1. `## Source` — LAST section: link to the closest real LeetCode problem.

## Hard rules

- **No function name anywhere in the doc.** No `def` stubs, no "write a
  function called X". The candidate names their own function. (Class
  definitions in `## Reference` are the only code.)
- **Source link goes at the bottom**, never under the title — a source link
  up top spoils the pattern before the story is read.
- **No `Difficulty:` label.** Interviewers don't announce difficulty.
- **No complexity-evaluation boilerplate.** Never include "Evaluate the time
  and space complexity of your solution…" or any variant — complexity
  discussion happens live in the interview, not in the prompt.
- **No meta hints** ("this tests BFS", "hint: use two pointers"). Prompt-only.
- **Never name the underlying LeetCode problem or pattern in the prose.**
- Story must be a real disguise: rename every entity (nodes → services,
  array → trade log, capacity → daily limit), not just a themed intro
  sentence on top of the bare prompt.

## Multi-part problems

A later problem may continue an earlier problem's story as a much harder
"Part 2" (e.g. LC 863 distance-k → LC 2385 infection time). Title it
`Part 2 — <subtitle>`, open by referencing the earlier incident, and change
the input contract slightly (e.g. node reference → bare ID) so the earlier
solution doesn't drop in unchanged.

## File conventions (this repo)

- Layout: `mock-interviews/<company>/NN_interview/` with
  `docs/01_<COMPANY>_MOCK_INTERVIEW.md` (index: title + source per problem),
  `docs/PROB_NN.md`, and `probNN.py` stubs.
- Stubs use the generic `probNN` function name with typed signature and
  `pass` body; include the Reference class in the stub file when needed.
- Superday companies use `NN_superday` with `## Interview #N` headers.

## Common mistakes

| Mistake                                | Fix                                             |
| -------------------------------------- | ----------------------------------------------- |
| Source/LeetCode link under the title   | Move to `## Source` at the very end             |
| "Write a function `foo(...)`" in prose | Plain directive: "Return the …"                 |
| Difficulty or pattern named            | Delete it                                       |
| Themed intro + verbatim LeetCode body  | Rename every entity in examples/constraints too |
| Explanation prose after the code fence | Move it inside the fence as `Explanation:`      |
