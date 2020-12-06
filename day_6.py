from utils import run, ident
from typing import List

@run(ident, '\n\n')
def day_6_1(groups: List[str]):
    return sum(len(set.union(*({*line} for line in group.split()))) for group in groups)


@run(ident, '\n\n')
def day_6_2(groups: List[str]):
    return sum(len(set.intersection(*({*line} for line in group.split()))) for group in groups)


if __name__ == '__main__':
    print("anyone:", day_6_1())
    print("everyone:", day_6_2())
