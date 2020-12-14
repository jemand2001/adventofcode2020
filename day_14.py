from utils import run, split_at
from typing import List

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
            print(f'relevant mask: {mask[-len(value):]}')
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


if __name__ == '__main__':
    print('sum of all values in memory:', day_14_1())
