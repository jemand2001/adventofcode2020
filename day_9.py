from utils import run
from typing import List

@run()
def day_9_1(numbers: List[int]):
    for i in range(25, len(numbers)):
        num = numbers[i]
        previous = set(numbers[i-25:i])
        if not any(num - k in previous for k in previous):
            return i, num
    return 0

@run()
def day_9_2(numbers: List[int]):
    for length in range(2, len(numbers)):
        for i in range(25, len(numbers) - length):
            consideration = numbers[i:i + length + 1]
            if sum(consideration) == 133015568:
                return i, i + length + 1, max(consideration) + min(consideration)


if __name__ == '__main__':
    print("first invalid:", day_9_1())
    print("weakness:     ", day_9_2())
