from utils import run, split_at, test
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
            print('new mask:', mask)
        else:
            address = int(register.split('[')[1][:-1])
            value = list(bin(int(value))[2:])
            print(f'value before:  {"".join(value)}')
            value.reverse()
            for i, x in enumerate(reversed(mask)):
                if i >= len(value):
                    value.append(x if x != 'X' else '0')
                if x == 'X':
                    continue
                value[i] = x
            value.reverse()
            print(f'value after:   {"".join(value)}')
            real = int(''.join(value), 2)
            print(f'(real):        {real}')
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
            print(f'new mask:   >>> {mask} <<<')
        else:
            address = list(bin(int(register.split('[')[1][:-1]))[2:])
            value = int(value)
            print(f'address before: {"".join(address).rjust(36, "0")}')
            print(f'current mask:   {mask}')
            address.reverse()
            for i, x in enumerate(reversed(mask)):
                if i >= len(address):
                    address.append(x)
                if x == '0':
                    continue
                address[i] = x
            address.reverse()
            print(f'address after:  {"".join(address).rjust(36, "0")}')
            for i in get_addresses(address):
                print(f'changing:       {bin(i)[2:].rjust(36, "0")}')
                mem[i] = value
    return sum(mem.values())


if __name__ == '__main__':
    print('sum of all values in memory:', day_14_1())
    print('sum of all values in memory:', day_14_2())
