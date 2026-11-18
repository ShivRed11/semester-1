# Reference solution (rewritten after original work was lost)

# Week 1.7, Session 1: Task 1

Equivalent classes for `process_data()`.

Hint: consider both positive and negative integers

| list data | Values |
| --- | --- |
| Empty list | `[]` -> expected `None` |
| Single integer list  | `[5]` -> `5`, `[-5]` -> `-5`, `[0]` -> `0` |
| Multiple integer list | `[1, 2, 3]` -> `6`, `[-1, -2, -3]` -> `-6`, `[-4, 10, 2]` -> `8`, `[5, -5]` -> `0` |

Note: `[0]` and `[5, -5]` are worth testing because the sum is 0, which is
"falsy" in Python - the function should still return `0`, not `None`.
