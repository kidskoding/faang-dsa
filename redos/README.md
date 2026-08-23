# Redos

A redo is the second attempt at a problem you needed help with the first time.
The original solution stays untouched in its module; the redo lives here under
the date you did it, so you can diff the two afterwards.

```text
redos/
└── 2026-08-22/
    ├── redo_problems.py
    └── tests/
        └── test_redo_problems.py
```

## The Rule

Write it from scratch. Do not open the original, the notes, or the Notion row
before you finish. A redo you peeked at teaches nothing — the point is finding
out what survived three days without rehearsal.

## Workflow

1. Notion `Problems to Review` → the **Due Now** tab tells you what is due.
2. Make `redos/YYYY-MM-DD/` with a `redo_problems.py` and a `tests/` beside it.
   Copy the assertions from the module's own test file.
3. Add the new folder to `pythonpath` in `pyproject.toml`.
4. Write each problem cold, then run it:
   ```bash
   uv run pytest redos -q
   ```
5. Compare against your first attempt:
   ```bash
   diff <(sed -n '/def longest_consecutive/,/^def /p' 01_arrays_and_hashing/problem_set/hashing_problems.py) \
        <(sed -n '/def longest_consecutive/,/^def /p' redos/2026-08-22/redo_problems.py)
   ```
6. Update Notion: clean on the first try → `Mastered`. Stumbled → keep it
   `Needs review`, push the date out three days, and rewrite the note with what
   slipped *this* time.

## Reading The Diff

| Result                | Meaning                                              |
| --------------------- | ---------------------------------------------------- |
| identical             | the pattern is internalized                          |
| different but correct | better still — you can solve it two ways             |
| needed a hint again   | not learned; requeue and note the step that vanished |

Keep the old dated folders. Three attempts at the same problem show you whether
it is converging or whether you are relearning it from scratch every time.
