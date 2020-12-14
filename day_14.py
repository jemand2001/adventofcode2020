from utils import run, split_at
from typing import List, Iterator

examples = ('''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1''',)

@run(split_at(' = '))
def day_14_1(program: List[List[str]]):
    mask = 'X' * 36
    mem = {}
    for register, value in program:
        if register == 'mask':
            mask = value
        else:
            address = int(register.split('[')[1][:-1])
            value = list(bin(int(value))[2:])
            value.reverse()
            for i, x in enumerate(reversed(mask)):
                if i >= len(value):
                    value.append(x if x != 'X' else '0')
                if x == 'X':
                    continue
                value[i] = x
            value.reverse()
            real = int(''.join(value), 2)
            mem[address] = real
    return sum(mem.values())

def get_addresses(address: List[str]) -> Iterator[int]:
    if 'X' not in address:
        yield int(''.join(address), 2)
    else:
        i = address.index('X')
        tmp = address.copy()
        tmp[i] = '0'
        yield from get_addresses(tmp)
        tmp[i] = '1'
        yield from get_addresses(tmp)

@run(split_at(' = '))
# @test(split_at(' = '), examples=examples)
def day_14_2(program: List[List[str]]):
    mask = 'X' * 36
    mem = {}
    for register, value in program:
        if register == 'mask':
            mask = value
        else:
            address = list(bin(int(register.split('[')[1][:-1]))[2:])
            value = int(value)
            address.reverse()
            for i, x in enumerate(reversed(mask)):
                if i >= len(address):
                    address.append(x)
                if x == '0':
                    continue
                address[i] = x
            address.reverse()
            for i in get_addresses(address):
                mem[i] = value
    return sum(mem.values())


if __name__ == '__main__':
    print('sum of all values in memory:', day_14_1())
    print('sum of all values in memory:', day_14_2())
