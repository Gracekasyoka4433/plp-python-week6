# PLP Python Week 6 - Error Handling

## Files

* `safe_tools.py` - Contains three safe functions that handle division by zero, invalid number conversion, and missing dictionary fields.
* `unbreakable.py` - Demonstrates how try/except can handle invalid user input and keep a Python program from crashing.

## Why can the if check not catch abc on its own?

An `if` check can test a condition, but it does not automatically prevent `int("abc")` from raising an error. The `int()` conversion raises a `ValueError`, so `try`/`except` is needed to catch the error and keep the program running.
