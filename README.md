# Advent of code 2020

This repository contains some utilities as well as my own solutions for [advent of code](https://adventofcode.com).

Please, for your sake, *DO NOT* use the solutions if you don't understand them.

#### How to use `run`
`utils.run` is a function that takes a conversion function and returns a decorator that will call the decorated function
with the inputs converted to the correct format. Usually this will be something like `int` or `utils.identity`.

The name of the decorated function should be of format `prefix_<day>`, as the decorator uses it to generate the correct
download link.

To use it, you need a separate file `env.py` with a variable `COOKIE` that contains your session cookie for advent of
code (because everyone's input is different)

```python
from utils import run
@run(int)
def solution_1(some_list):
    return some_list[0]
```
