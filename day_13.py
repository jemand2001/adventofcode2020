from utils import run, ident, test
from typing import List
from itertools import count
from numpy import lcm
from functools import reduce

examples = ('''
17,x,13,19''', '''
67,7,59,61''', '''
67,x,7,59,61''', '''
67,7,x,59,61''', '''
1789,37,47,1889''',
            )

@run(ident)
def day_13_1(schedule: List[str]):
    earliest = int(schedule[0])
    buses = [int(i) for i in schedule[1].split(',') if i != 'x']
    for i in count(earliest):
        for bus in buses:
            if not i % bus:
                return bus * (i - earliest)

def congruent(a, b):
    # return lambda x: x % b == a % b
    def f(x):
        # print(f'considering {x}')
        return x % b == a % b
    return f

@run(ident)
# @test(ident, examples=examples)
def day_13_2(schedule: List[str]):
    # buses = [int(i) for i in schedule[1].split(',') if i != 'x']
    buses = [
        (int(bus), int(bus) - off)
        for off, bus in enumerate(schedule[1].split(','))
        if bus != 'x'
    ]
    buses.sort(key=lambda b: b[0], reverse=True)
    start = 100000000000000
    while not congruent(*buses[0])(start):
        start += 1
    possible = count(start, buses[0][0])
    for n, a in buses[1:]:
        possible = filter(congruent(a, n), possible)
    return next(possible)

def egcd(a, b):
    if a == 0:
        return 0, 1
    else:
        x, y = egcd(b % a, a)
        return y - (b//a) * x, x

def solve(a1, n1, a2, n2):
    m1, m2 = egcd(n1, n2)
    return a1 * m2 * n2 + a2 * m1 * n1

@test(ident, examples=examples)
def day_13_2_exist(schedule: List[str]):
    buses = [
        (int(bus), int(bus) - off)
        for off, bus in enumerate(schedule[1].split(','))
        if bus != 'x'
    ]
    buses.sort(key=lambda b: b[0], reverse=True)
    current = 0
    while len(buses) > 1:
        b = buses.pop(0)
        step = b[1] * buses[0][1]
        current = solve(*b, *buses[0])
        while current < 0:
            current += step
        buses[0] = (current, step)
    return current

@run(ident)
# @test(ident, examples=examples)
def day_13_2_jenna(schedule: List[str]):
    """Source for this code: @jenna#8484 on Captain Disillusion's discord server"""
    buses = [
        (off, int(bus))
        for off, bus in enumerate(schedule[1].split(','))
        if bus != 'x'
    ]
    m = 1
    for _, bus in buses:
        m *= bus
    result = 0
    for offset, bus in buses:
        a, b = egcd(bus, m // bus)
        result += (bus - offset) * b * m // bus
    return result % m


if __name__ == '__main__':
    # print('id * time:', day_13_1())
    print('time:', day_13_2_jenna())
