______________________________________________________________________

## name: problem-set-tests-scaffold description: Use when adding or mirroring a module problem_set and its pytest suite in this DSA repo (e.g. "mirror the trees problem set for X", "scaffold a problem set for heaps", "write the tests file"), to reproduce the exact folder layout, stub header format, test helper convention, namespace-package import style, and pyproject pythonpath wiring.

# Problem Set + Tests Scaffold

The mechanical convention for a module `problem_set/` and its `tests/` in this repo. The canonical reference implementations live in `07_trees/` (solved) and `06_linked_lists/` (stubs). This skill is the layer below `dsa-module-workbooks`: that skill decides *which problems* and the workbook prose; this one nails the *exact files, imports, and config* so the suite collects and runs.

## When To Use

- "Mirror the `<module>` problem set / tests for `<other module>`."
- "Scaffold a problem set and tests for `<module>`."
- "Write the tests file" for an existing `problem_set/`.

For problem selection, banding (Fundamentals / Mediums / Hards), and workbook markdown rules, use `dsa-module-workbooks`. This skill assumes the problem list already exists or is being chosen there.

## Folder Layout

```text
NN_module/
├── <node_module>.py                 # shared node class, e.g. list_node.py, tree_node.py (already exists)
├── problem_set/
│   ├── MODULE_PROBLEM_SET.md         # workbook index (see dsa-module-workbooks)
│   ├── <category_a>_problems.py      # stubs grouped by pattern
│   ├── <category_b>_problems.py
│   └── ...
└── tests/
    ├── conftest.py                   # empty file
    ├── test_<category_a>_problems.py
    ├── test_<category_b>_problems.py
    └── ...
```

- **No `__init__.py` anywhere.** `problem_set` resolves as an implicit namespace package across modules — that is why two modules can both have a `problem_set/`.
- One category `.py` per pattern family; one test file per category, named `test_<category>.py`.
- One function per problem. Group functions by the workbook's bands/categories.

## Stub File Format

Each category file imports the shared node class and holds one function per problem. Header comment carries the problem number, the key idea, and empty complexity lines. Body is `pass`.

```python
from list_node import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    # Problem 1: Reverse Linked List
    # Key idea: walk the list flipping each next pointer.
    # Time:
    # Space:

    pass
```

- Import the node by bare module name: `from list_node import ListNode`, `from tree_node import TreeNode`. This works because the module dir is on `pythonpath` (see below).
- Type-hint every signature (`ListNode | None`, `list[int]`, etc.).
- In-place problems return `None`; reflect that in the hint and the docs example.
- Problems needing their own node type (e.g. random-pointer, multilevel, an LRU class) define that class at the top of the category file with a comment naming the problem it serves. Put `from __future__ import annotations` first when the class self-references.
- Use `pass` as the body, never `raise NotImplementedError`, so unimplemented functions return `None` and tests fail as clean assertions, not errors.

### Modules Without A Node Class

Some modules have no shared node module — heaps use `heapq`, arrays/DP/intervals take plain `list[int]`. For these:

- Omit the `from <node> import ...` line; stubs take/return plain types (`list[int]`, `int`, `bool`).
- Skip the inline `build_*`/`to_*` helpers — there is nothing to construct or serialize; pass literals straight in.
- You **still** add the module dir to `pythonpath` — it is required for the `from problem_set.<category>_problems import ...` package import to resolve, independent of any node import.

## Test File Format

Mirror `07_trees/tests/`: per-category test files, helpers defined **inline** in each file (not shared), empty `conftest.py`.

```python
from list_node import ListNode
from problem_set.traversal_problems import reverse_list, merge_two_lists


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    curr = dummy
    for value in values:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def test_reverse_list_multiple():
    assert to_list(reverse_list(build_list([1, 2, 3]))) == [3, 2, 1]
```

- Import functions from the package: `from problem_set.<category>_problems import ...`.
- Import the node by bare name: `from <node_module> import Node`.
- Define construction/serialization helpers (`build_list`/`to_list`, `build_sample_tree`, etc.) **inline per test file**. Trees repeats them; match that — do not factor into `conftest.py`.
- `conftest.py` stays **empty** (it just marks the dir for pytest path handling).
- Cover empty, single, normal, and edge/skewed cases per problem. Use one shared representative input across related tests when it reads cleanly.
- Test identity with `is` where the contract returns an existing node (cycle entry, intersection node); compare values via `to_list` otherwise.

## pyproject Wiring (the step that is easy to miss)

`pyproject.toml` at repo root drives collection. Two arrays matter:

```toml
[tool.pytest.ini_options]
pythonpath = [
    "06_linked_lists",
    "07_trees",
    # add "NN_module" so `from <node> import X` and `from problem_set.X import Y` resolve
]
testpaths = [
    # numbered modules already listed here; confirm NN_module is present
]
```

- **Add the module dir to `pythonpath`** or every import in the new files fails to resolve. This is the most common scaffold mistake.
- `testpaths` already lists all numbered modules; just confirm the target is there.
- No other config needed — namespace packages mean no `__init__.py`, no setup.

## Verify

```bash
python3 -m pytest NN_module/tests -q
```

Expect a clean collection. If the stubs are unimplemented (`pass`), tests are **RED on purpose** — they are the target for solving. Confirm the count and that failures are assertion failures, not `ImportError`/collection errors. An `ImportError` means `pythonpath` is missing the module dir.

## Common Mistakes

| Mistake                                              | Symptom                                                        | Fix                                                                             |
| ---------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Forgot `pythonpath` entry                            | `ModuleNotFoundError: list_node` / `problem_set` at collection | Add `"NN_module"` to `pythonpath` in pyproject                                  |
| Added `__init__.py`                                  | `problem_set` from another module shadows / import clashes     | Delete it; rely on namespace packages                                           |
| Shared helpers in `conftest.py`                      | Diverges from trees convention                                 | Inline `build_*`/`to_*` in each test file                                       |
| `NotImplementedError` body                           | Tests error instead of asserting                               | Use `pass` so failures are clean assertion RED                                  |
| Compared nodes by value when contract returns a node | False pass/fail on cycle/intersection                          | Assert with `is` against the expected node                                      |
| Renamed category files per test run                  | Imports drift                                                  | Keep `<category>_problems.py` ↔ `test_<category>_problems.py` paired and stable |
