from utils import run, ident
from typing import List, Tuple
from operator import add, mul
import re

examples = (
    '''1 + 2 * 3 + 4 * 5 + 6''',
    '''1 + (2 * 3) + (4 * (5 + 6))''',
    '''2 * 3 + (4 * 5)''',
    '''5 + (8 * 3 + 9 + 3 * 4 * 3)''',
    '''5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))''',
    '''((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2''',
)

operators = {'*': mul, '+': add}

def parse_equal(line: str) -> Tuple[int, int]:
    res = 0
    next_op = add
    i = 0
    while i < len(line):
        c = line[i]
        if c.isdigit():
            res = next_op(res, int(c))
        elif c in operators:
            next_op = operators[c]
        elif c == '(':
            k, skipped = parse_equal(line[i + 1:])
            res = next_op(res, k)
            i += skipped + 1
        elif c == ')':
            return res, i
        else:
            raise ValueError(c)
        i += 1
    return res, len(line)

def parse_pluses(line: str) -> int:
    while match := re.fullmatch(r'(?P<prefix>.*?)\((?P<parens>[^()]+)\)(?P<suffix>.*)', line):
        line = match['prefix'] + str(parse_pluses(match['parens'])) + match['suffix']
    line = re.sub(r'(\d+(?: \+ \d+)+)', lambda m: str(eval(m[0])), line)
    return eval(line)

@run(ident)
def day_18_1(lines: List[str]):
    return sum(parse_equal(line.replace(' ', ''))[0] for line in lines)

@run(ident)
def day_18_2(lines: List[str]):
    return sum(parse_pluses(line) for line in lines)


if __name__ == '__main__':
    print('sum of all expressions (equal):', day_18_1())
    print('sum of all expressions (pluses):', day_18_2())
