# Projects

This folder is scoped to **practical projects only** — nothing here is a tutorial, a code snippet, or a theory writeup. Every folder is a small, hands-on build tied to a specific topic (or a mix of topics once a combo project is added).

## What belongs here

- **Topical projects** — each one targets a single concept area (e.g. basics, flow control, functions) and is numbered in the order it should be attempted.
- **Combination projects** — once enough standalone topics exist, later folders will deliberately combine two or more of them (e.g. flow control + functions, or functions + file I/O) into one bigger build. These will be numbered after the topics they depend on and will say so in their own `README.md`.

Nothing else goes in this folder — no notes, no isolated exercises, no reference docs. If it isn't a runnable project with its own `README.md`, it doesn't belong here.

## Structure

Each project is its own folder:

```text
NN-topic-name/
  README.md      # problem statement, expected outcome, hint
  <your code>    # your own implementation, not committed as a "solution"
```

Combination projects follow the same structure, just with a `README.md` that lists which prior topics it draws on.

## Current projects

| # | Topic | Folder |
| --- | ------- | -------- |
| 1 | Python Basics | [`01-python-basics/`](./01-python-basics) |
| 2 | Flow Control | [`02-flow-control/`](./02-flow-control) |
| 3 | Functions | [`03-functions/`](./03-functions) |

New topical folders will keep extending this numbering; combination projects will be added once there's enough topic coverage to combine.
