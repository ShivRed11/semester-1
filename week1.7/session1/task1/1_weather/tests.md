# Reference solution (rewritten after original work was lost)

# Week 1.7, Session 1: Task 1

Equivalent classes for `comfort_level()`

| Comfort level | Values |
| --- | --- |
| COLD | -10.0, 0.0, 15.0 (boundary: 15.0 is still COLD because the test is `<= 15.0`) |
| HOT  | 25.1 (just over the boundary), 30.0, 40.0 |
| OK   | 15.1 (just over the COLD boundary), 20.0, 25.0 (boundary: 25.0 is still OK because HOT needs `> 25.0`) |

Key idea: pick one "typical" value from the middle of each class, plus the
values either side of each boundary (15.0 / 15.1 and 25.0 / 25.1), because
off-by-one style mistakes (`<` vs `<=`) happen at the edges.
