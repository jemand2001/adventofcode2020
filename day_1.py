from utils import run
from typing import Iterable, Union
from itertools import product
from functools import reduce
from operator import mul


@run(int)
def day_1_1(expenses: Iterable[int]) -> int:
    for i, j in product(expenses, repeat=2):
        if i + j == 2020:
            return i * j


@run(int)
def day_1_2(expenses: Iterable[int], k) -> int:
    for t in product(expenses, repeat=k):
        if sum(t) == 2020:
            return reduce(mul, t)


@run(int)
def day_1_golf(expenses: Iterable[int], k) -> int:
    return reduce(mul, [i for i in product(expenses, repeat=k) if sum(i) == 2020])


if __name__ == '__main__':
    for i in range(2, 4):
        print(i, day_1_2(i), sep=': ')
