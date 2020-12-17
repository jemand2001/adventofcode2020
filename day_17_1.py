from utils import run
from typing import List, Set, Iterator
from collections import namedtuple

examples = ('''\
.#.
..#
###''',)

Point = namedtuple('Point', ('x', 'y', 'z'))
Dimension = Set[Point]


def all_points(start: Point, end: Point) -> Iterator[Point]:
    for z in range(start.z, end.z + 1):
        for y in range(start.y, end.y + 1):
            for x in range(start.x, end.x + 1):
                yield Point(x, y, z)

def neighbors(p: Point) -> Iterator[Point]:
    yield from filter(lambda x: x != p, all_points(
        Point(p.x - 1, p.y - 1, p.z - 1),
        Point(p.x + 1, p.y + 1, p.z + 1)
    ))

def minimum(d: Dimension) -> Point:
    return Point(
        min(p.x for p in d) - 1,
        min(p.y for p in d) - 1,
        min(p.z for p in d) - 1
    )

def maximum(d: Dimension) -> Point:
    return Point(
        max(p.x for p in d) + 2,
        max(p.y for p in d) + 2,
        max(p.z for p in d) + 2
    )

def cycle(previous: Dimension) -> Dimension:
    active: Dimension = set()
    for point in all_points(minimum(previous), maximum(previous)):
        if point in previous and sum(p in previous for p in neighbors(point)) in (2, 3):
            active.add(point)
        elif point not in previous and sum(p in previous for p in neighbors(point)) == 3:
            active.add(point)
    return active


@run(list)
def day_17_1(start: List[List[str]]):
    active: Dimension = set()
    for y, row in enumerate(start):
        for x, _ in enumerate(row):
            if start[y][x] == '#':
                active.add(Point(x, y, 0))
    print('cycle: 0')
    show_cubes(active)
    for i in range(1, 7):
        active = cycle(active)
        print(f'cycle: {i}')
        show_cubes(active)
    return len(active)

def show_cubes(d: Dimension):
    low = minimum(d)
    high = maximum(d)
    for z in range(low.z, high.z):
        print(f'z = {z}')
        for y in range(low.y, high.y):
            print(''.join('.' if (x, y, z) not in d else '#' for x in range(low.x, high.x)))


if __name__ == '__main__':
    print('active after 6 cycles:', day_17_1())
