from utils import run, ident
from typing import List, Tuple
from operator import add, mul

examples = (
    '''1 + 2 * 3 + 4 * 5 + 6''',
    '''1 + (2 * 3) + (4 * (5 + 6))''',
    '''2 * 3 + (4 * 5)''',
    '''5 + (8 * 3 + 9 + 3 * 4 * 3)''',
    '''5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))''',
    '''((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2''',
)

operators = {'*': mul, '+': add}

def parse_expression_equal(line: str) -> Tuple[int, int]:
    res = 0
    next_op = add
    i = 0
    while i < len(line):
        c = line[i]
        if ord('0') <= ord(c) <= ord('9'):
            res = next_op(res, int(c))
        elif c in operators:
            next_op = operators[c]
        elif c == '(':
            print('descending!')
            k, skipped = parse_expression_equal(line[i + 1:])
            res = next_op(res, k)
            i += skipped + 1
        elif c == ')':
            return res, i
        else:
            raise ValueError(c)
        i += 1
    return res, len(line)

@run(ident)
def day_18_1(lines: List[str]):
    return sum(parse_expression_equal(line.replace(' ', ''))[0] for line in lines)



if __name__ == '__main__':
    print('sum of all expressions (equal):', day_18_1())
