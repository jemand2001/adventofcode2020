from utils import run, part
from typing import List

def coordinates(row: str, col: str):
    return int(row.replace('F', '0').replace('B', '1'), base=2), int(col.replace('L', '0').replace('R', '1'), base=2)

def pid(row: int, col: int):
    return row * 8 + col

def make_pid(s: str):
    return pid(*coordinates(*part(7)(s)))

@run(make_pid)
def day_5_1(pids: List[int]):
    return max(pids)

@run(make_pid)
def day_5_2(pids: List[int]):
    pids = set(pids)
    return [i + 1 for i in pids if i + 1 not in pids and i + 2 in pids][0]


if __name__ == '__main__':
    print('highest ID:', day_5_1())
    print('your ID is:', day_5_2())
