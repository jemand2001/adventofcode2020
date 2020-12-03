from utils import run, ident
from functools import reduce
from operator import mul


@run(ident)
def day_3_1(forest):
    y_size = len(forest)
    tile_size = len(forest[0])
    x = y = 0
    trees = 0
    while y < y_size - 1:
        x = (x + 3) % tile_size
        y += 1
        # print(f'({x}/{y}) ∈ ({tile_size}/{y_size})?')
        trees += forest[y][x] == '#'
    return trees


@run(ident)
def day_3_2(forest, slope):
    y_size = len(forest)
    tile_size = len(forest[0])
    x_step, y_step = slope
    x = y = 0
    trees = 0
    while y < y_size - y_step:
        x = (x + x_step) % tile_size
        y += y_step
        trees += forest[y][x] == '#'
    print(f'{slope}: {trees} trees')
    return trees


from itertools import count
@run(ident)
def day_3_golf(forest):
    return reduce(mul, (sum(forest[y][x % len(forest[0])] == '#' for x, y in zip(count(0, dx),
                                                                                 range(0, len(forest), dy)))
                        for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))


if __name__ == '__main__':
    print(reduce(mul,
                 (
                     day_3_2(slope) for slope in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
                 )
                 ))

    print(day_3_golf())
