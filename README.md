# Django Signals and Custom Classes

## Django Signals

### Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer:** Django signals are executed **synchronously** by default.

**Proof:** The `TestSignalsSynchronicity` test case demonstrates this. It measures the time taken to execute a signal that includes a 5-second sleep. The test asserts that the total response time is greater than 5 seconds, confirming that the signal is executed within the request-response cycle and not in a separate thread or process.

### Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer:** Yes, Django signals run in the **same thread** as the caller.

**Proof:** The `TestSignalsThread` test case captures the thread ID of the caller and compares it with the thread ID within the signal handler. The test asserts that both IDs are the same, confirming that the signal handler executes in the caller thread.

### Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

**Answer:** No, Django signals do not run in the same **database transaction** as the caller by default.

**Proof:** The `TestSignalTransaction` test case attempts to delete a user within a transaction. The signal handler associated with the delete operation raises an exception. The test asserts that the user is deleted (because the user.delete() call happens before the signal) but the associated profile remains (because the signal's exception rolls back the profile deletion). This proves that the signal handler runs in a separate transaction.

## Custom Classes in Python

**Task:** Create a `Rectangle` class with the following requirements:

-   Initialization with `length: int` and `width: int`.
-   Iterable, yielding length first in the format `{'length': <value>}`, then width in the format `{'width': <value>}`.

**Solution:**

The `Rectangle` class is implemented in `app/rectangle.py`

```
class Rectangle:
    length: int
    width: int

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}
```

A test case (`TestRectangle`) has been created to verify the correctness of the Rectangle class.
