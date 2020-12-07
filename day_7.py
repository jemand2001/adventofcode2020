from utils import run, split_at
from typing import List, Dict, Tuple, Callable, TypeVar, Hashable, Generic
from operator import mul, add
from collections import defaultdict

H = TypeVar('H', bound=Hashable)
union = set.union

def find_trans(graph: Dict[str, List[str]], to_search):
    potentials = {color for color, inner in graph.items() if to_search in inner}
    changed = True
    while changed:
        current = set()
        for i in potentials:
            current.update({color for color, inner in graph.items() if i in inner} - potentials)
        changed = len(current) != 0
        potentials.update(current)
    return potentials

def parse_rules(lines: List[Tuple[str, str]]):
    rules: Dict[str, List[str]] = {}
    for outer, inner in lines:
        colors = []
        if inner != 'no other bags.':
            for i in inner.split(','):
                _, color = i.split(maxsplit=1)
                colors.append(color.rsplit(maxsplit=1)[0])
        rules[outer.rsplit(maxsplit=1)[0]] = colors
    return rules

@run(split_at(' contain '))
def day_7_1(lines: List[Tuple[str, str]]):
    return len(find_trans(parse_rules(lines), 'shiny gold'))

def combine(*ds: Dict[str, int]) -> Dict[str, int]:
    return {k: sum(d.get(k, 0) for d in ds) for k in union(*(set(d.keys()) for d in ds))}

def multiply(i: int, d: Dict[H, int]) -> Dict[H, int]:
    return {k: v * i for k, v in d.items()}

def explore(rules: Dict[str, Dict[str, int]], origin: str) -> Dict[str, int]:
    d = {}
    for i, v in rules[origin].items():
        print(f"{i}: {v}")
        d = combine(d, {i: v}, multiply(v, explore(rules, i)))
    print(d)
    return d

def day_7_2_inner(lines: List[Tuple[str, str]]):
    rules: Dict[str, Dict[str, int]] = {}
    for outer, inner in lines:
        d = {}
        if inner != 'no other bags.':
            for i in inner.split(','):
                count, color = i.split(maxsplit=1)
                d[color.rsplit(maxsplit=1)[0]] = int(count)
        rules[outer.rsplit(maxsplit=1)[0]] = d
    return sum(explore(rules, 'shiny gold').values())


day_7_2 = run(split_at(' contain '))(day_7_2_inner)


if __name__ == '__main__':
    print("containing shiny gold:", day_7_1())
    print("contained in shiny gold:", day_7_2())
