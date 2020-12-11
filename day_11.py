from utils import run
from typing import List, Set, Tuple

def count_adjacent(occupied: Set[Tuple[int, int]], row: int, col: int):
    return sum((row + r_off, col + c_off) in occupied for c_off in range(-1, 2) for r_off in range(-1, 2)
               if not (c_off == 0 and r_off == 0))

@run(list)
def day_11_1(seats: List[List[str]]):
    occupied = set()
    changed = True
    while changed:
        changed = False
        print(occupied)
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


if __name__ == '__main__':
    print("occupied seats:", day_11_1())
