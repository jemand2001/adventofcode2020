from utils import run, ident
from typing import List, Dict, Tuple
from collections import defaultdict
from functools import reduce
from operator import mul

def parse_fields(lines: str) -> Dict[str, List[int]]:
    res = defaultdict(list)
    for line in lines.split('\n'):
        key, values = line.split(':')
        ranges = values.split(' or ')
        for k in ranges:
            res[key].extend(range(int((r := k.split('-'))[0]), int(r[1]) + 1))
    return dict(res)

def parse_ticket(line: str) -> List[int]:
    return [*map(int, line.split(','))]

def invalid(fields: Dict[str, List[int]], value: int) -> bool:
    return not any(value in possible for possible in fields.values())

@run(ident, '\n\n')
def day_16_1(parts: List[str]):
    fields = parse_fields(parts[0])
    others = [parse_ticket(line) for line in parts[2].split('\n')[1:]]
    return sum(sum(value for value in ticket if invalid(fields, value)) for ticket in others)

@run(ident, '\n\n')
def day_16_2(parts: List[str]):
    fields = parse_fields(parts[0])
    mine = parse_ticket(parts[1].split('\n')[1])
    others = [parse_ticket(line) for line in parts[2].split('\n')[1:]]
    others = [ticket for ticket in others if not any(invalid(fields, value) for value in ticket)]
    positions: Dict[str, Tuple[bool, List[int]]] = {}
    for k, v in fields.items():
        possible = [idx for idx, _ in enumerate(mine) if all(ticket[idx] in v for ticket in others)]
        positions[k] = False, possible
    while any(len(i[1]) > 1 for i in positions.values()):
        key, current = next((k, v[0]) for k, (checked, v) in positions.items() if len(v) == 1 and not checked)
        for k, (checked, v) in positions.items():
            if k != key and current in v and len(v) > 1:
                v.remove(current)
        positions[key] = True, [current]
    return reduce(mul, (mine[positions[key][1][0]] for key in fields if key.startswith('departure')))


if __name__ == '__main__':
    print('error rate:', day_16_1())
    print('other tickets:', day_16_2())
