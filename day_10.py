from utils import run, test
from typing import List, Tuple
from collections import Counter
from functools import lru_cache

examples = ("""16
10
15
5
1
11
7
19
6
12
4""", """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""")

# @test(examples=examples)
@run()
def day_10_1(adapters: List[int]):
    adapters.sort()
    # phone = adapters[-1] + 3
    # print("phone adapter:", phone)
    differences = Counter()
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    while len(adapters) > 1:
        current = adapters.pop(0)
        next_adapter = adapters[0]
        # print(f'current: {current}; next: {next_adapter}')
        differences += Counter([next_adapter - current])
    # differences += Counter([3])
    return differences[1] * differences[3]

@lru_cache(maxsize=None)
def combinations(adapters: Tuple[int], current):
    if current == adapters[-1]:
        return 1
    return sum(combinations(adapters, i) for i in adapters if current < i <= current + 3)

# @test(examples=examples)
@run()
def day_10_2(adapters: List[int]):
    adapters.sort()
    return sum(combinations(tuple(adapters), i) for i in adapters if i <= 3)


if __name__ == '__main__':
    # print("1-steps * 3-steps:", day_10_1())
    print("arrangements:", day_10_2())
