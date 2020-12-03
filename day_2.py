from utils import run
from typing import List


def is_valid_1(constraint: str, letter: str, password: str):
    minimum, maximum = map(int, constraint.split('-'))
    return minimum <= password.count(letter) <= maximum


def is_valid_2(args):
    constraint, letter, password = args
    letter = letter.strip(':')
    pos1, pos2 = map(int, constraint.split('-'))
    return (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter)


@run(str.split)
def day_2_1(lines: List[List[str]]):
    return len([
        password
        for [constraint, letter, password] in lines
        if is_valid_1(constraint, letter.strip(':'), password)
    ])


@run(str.split)
def day_2_2(lines: List[List[str]]):
    return sum(map(is_valid_2, lines))


if __name__ == '__main__':
    print("ranges:", day_2_1())
    print("positions:", day_2_2())
