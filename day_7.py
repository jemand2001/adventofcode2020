from utils import run, split_at
from typing import List, Dict, Tuple
from collections import defaultdict

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

@run(split_at(' contain '))
def day_7_2(lines: List[Tuple[str, str]]):
    rules = parse_rules(lines)
    potentials = set(rules['shiny gold'])
    changed = True
    while changed:
        current = set()
        for i in potentials:
            current.update(set(rules[i]) - potentials)
        changed = bool(len(current)) or 'shiny gold' not in current
    return len(rules)


if __name__ == '__main__':
    print("containing shiny gold:", day_7_1())
    print("contained in shiny gold:", day_7_2())
