# Accuknox Django Trainee Assignment

## Django Signals and Custom Classes

This repository contains code snippets and explanations related to Django signals and a custom Rectangle class in Python.

### Django Signals

**Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

Answer: By default, Django signals are executed synchronously.
Proof: See the `my_signal_handler` function inside `signals.py` for a code example demonstrating how a delay in the signal handler directly affects the overall execution time, confirming its synchronous nature.

**Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

Answer: Yes, Django signals run in the same thread as the caller by default.
Proof: The `my_signal_handler2` function inside `signals.py` file includes a code snippet that captures and compares the thread IDs of the caller and the signal handler, showcasing that they are identical.

**Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.**

Answer: Yes, Django signals operate within the same database transaction as the caller by default.
Proof: The `my_signal_handler_question3` function inside `signals.py` file contains code that triggers an error within a signal handler, leading to a rollback of the entire transaction, even for operations that occurred before the signal was triggered.

### Custom Rectangle Class

**Description: You are tasked with creating a Rectangle class with the following requirements:**

**An instance of the Rectangle class requires length:int and width:int to be initialized.**
**We can iterate over an instance of the Rectangle class**
**When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}**

File: `utils.py`
Description: The Rectangle class allows you to create rectangle objects with specified length and width. It supports iteration, yielding the length and width in a dictionary format.
Usage: See the example usage within utils.py to understand how to create and iterate over Rectangle instances.
