from utils import run, ident, test
from typing import List
from itertools import count
from numpy import lcm
from functools import reduce

examples = ('''
17,x,13,19''', '''
67,7,59,61''')

@run(ident)
def day_13_1(schedule: List[str]):
    earliest = int(schedule[0])
    buses = [int(i) for i in schedule[1].split(',') if i != 'x']
    for i in count(earliest):
        for bus in buses:
            if not i % bus:
                return bus * (i - earliest)

# @run(ident)
@test(ident, examples=examples)
def day_13_2(schedule: List[str]):
    buses = [int(i) for i in schedule[1].split(',') if i != 'x']
    # t = 100000000000000
    # while t % buses[0]:
    #     t += 1
    # while not all((t + n) % bus == 0 for n, bus in enumerate(buses)):
    #     print('trying:', t)
    #     t += buses[0]
    return reduce(lcm, (bus + offset for offset, bus in enumerate(buses)))


if __name__ == '__main__':
    # print('id * time:', day_13_1())
    print('time:', day_13_2())
