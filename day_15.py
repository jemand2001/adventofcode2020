from utils import run
from typing import List
from collections import defaultdict


def game(starting, stop):
    prev = defaultdict(list)
    for i, j in enumerate(starting, 1):
        prev[j].append(i)
    previous = starting[-1]
    for i in range(len(starting) + 1, stop):
        if len(prev[previous]) > 1:
            current = prev[previous][-1] - prev[previous][-2]
        else:
            current = 0
        prev[current].append(i)
        previous = current
    print(f'max number: {max(prev.keys())}')
    return previous

@run(sep=',', content='11,18,0,20,1,7,16')
def day_15_1(starting: List[int]):
    return game(starting, 2021)

@run(sep=',', content='11,18,0,20,1,7,16')
def day_15_2(starting: List[int]):
    return game(starting, 30000001)


if __name__ == '__main__':
    # print('2020th number:', day_15_1())
    print('30000000th number:', day_15_2())
