from utils import run
from typing import List, Set, Tuple

examples = ("""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""",)

def count_adjacent(occupied: Set[Tuple[int, int]], row: int, col: int):
    return sum((row + r_off, col + c_off) in occupied for c_off in range(-1, 2) for r_off in range(-1, 2)
               if not (c_off == 0 and r_off == 0))

@run(list)
def day_11_1(seats: List[List[str]]):
    occupied = set()
    changed = True
    while changed:
        changed = False
        previous = occupied
        occupied = set()
        for r_num, row in enumerate(seats):
            for c_num, seat in enumerate(row):
                if seat == 'L' and (r_num, c_num) not in previous:  # empty
                    if count_adjacent(previous, r_num, c_num) == 0:
                        occupied.add((r_num, c_num))
                        changed = True
                elif seat == 'L' and (r_num, c_num) in previous:
                    if count_adjacent(previous, r_num, c_num) < 4:
                        occupied.add((r_num, c_num))
                    else:
                        changed = True
        # changed = previous != occupied
    return len(occupied)

def count_visible(occupied: Set[Tuple[int, int]], row: int, col: int, seats):
    size_x = len(seats[0])
    size_y = len(seats)
    total = 0
    for dx, dy in ((0, 1), (1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1)):
        x, y = col + dx, row + dy
        while 0 <= x < size_x and 0 <= y < size_y:
            if seats[y][x] == 'L':
                if (x, y) in occupied:
                    total += 1
                break
            x += dx
            y += dy
    return total

@run(list)
def day_11_2(seats: List[List[str]]):
    occupied = set()
    changed = True
    while changed:
        changed = False
        print(occupied)
        previous = occupied
        occupied = set()
        for r_num, row in enumerate(seats):
            for c_num, seat in enumerate(row):
                if seat == 'L' and (c_num, r_num) not in previous:  # empty
                    if count_visible(previous, r_num, c_num, seats) == 0:
                        occupied.add((c_num, r_num))
                        changed = True
                elif seat == 'L' and (c_num, r_num) in previous:
                    if count_visible(previous, r_num, c_num, seats) < 5:
                        occupied.add((c_num, r_num))
                    else:
                        changed = True
    return len(occupied)


if __name__ == '__main__':
    print("occupied seats:", day_11_1())
    # print("occupied seats:", day_11_2())
