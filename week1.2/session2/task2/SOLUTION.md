<!-- Reference solution (rewritten after original work was lost) -->
# Task 2 - Solution

Start the interpreter with `python` (or `python3`), then type each expression:

| Expression | Result | Why |
|---|---|---|
| `not (3 > 1)` | `False` | `3 > 1` is True; `not` flips it |
| `(4 > 2) and (6 > 8)` | `False` | `and` needs BOTH sides True; `6 > 8` is False |
| `(5 == 5) or (2 > 10)` | `True` | `or` needs only ONE side True; `5 == 5` is True |
| `not (10 > 5 or 3 != 3)` | `False` | inside: True or False = True; `not` gives False |
| `5 < 10 < 15` | `True` | chained comparison = `5 < 10 and 10 < 15` |
| `3 <= 3 < 10 and (10 == 10 or 5 > 8)` | `True` | left: `3 <= 3 and 3 < 10` = True; right: True or False = True; True and True = True |

Exit with `Ctrl+D` (or `exit()`).
