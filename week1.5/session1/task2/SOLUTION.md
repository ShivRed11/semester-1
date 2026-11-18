<!-- Reference solution (rewritten after original work was lost) -->
# Task 2 - answers

## badclass1.py

Error:

    TypeError: Point.__init__() takes 2 positional arguments but 3 were given

**Cause:** `__init__` has no `self` parameter. When we write `Point(1.5, 2.0)`
Python automatically passes the new object as the first argument, so the
method actually receives 3 arguments (object, 1.5, 2.0) but only declares 2.
(pylint reports this as *"Method should have "self" as first argument"*.)

**Fix:** add `self` as the first parameter (and see the badclass2 fix too,
because the assignments are also wrong):

```python
def __init__(self, x_coordinate, y_coordinate):
    self.x = x_coordinate
    self.y = y_coordinate
```

## badclass2.py

Error:

    AttributeError: 'Point' object has no attribute 'x'

**Cause:** inside `__init__`, `x = x_coordinate` creates a *local variable*
called `x` that disappears when the method ends. It does not create a field
on the object, so `p.x` doesn't exist. (pylint reports these as *unused
variables*.)

**Fix:** assign to fields of the object via `self`:

```python
self.x = x_coordinate
self.y = y_coordinate
```

## Fixed class (works for both files)

```python
class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)    # 1.5
print(p.y)    # 2.0
```
