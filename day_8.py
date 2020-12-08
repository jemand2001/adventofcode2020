from utils import run, split_at
from typing import List, Tuple

def parse_instruction(line: str):
    i, arg = line.split(' ')
    return i, int(arg)

@run(parse_instruction)
def day_8_1(instructions: List[Tuple[str, int]]) -> int:
    visited = []
    current = 0
    acc = 0
    while current not in visited:
        visited.append(current)
        if instructions[current][0] == 'jmp':
            current += instructions[current][1]
            continue
        if instructions[current][0] == 'nop':
            pass
        elif instructions[current][0] == 'acc':
            acc += instructions[current][1]
        current += 1
    return acc

@run(parse_instruction)
def day_8_2(instructions: List[Tuple[str, int]]) -> int:
    visited = []
    changed = None
    tried = set()
    current = 0
    acc = 0
    while current < len(instructions):
        visited.append(current)
        instruction, arg = instructions[current]
        if instruction == 'jmp':
            if current + arg not in visited:
                if changed is None and current not in tried:
                    changed = current, acc
                    tried.add(changed)
                    current += 1
                else:
                    current, acc = changed
                    changed = None
                continue
        if instruction == 'nop':
            if current + 1 in visited and current + arg >= len(instructions):
                if changed is None and current not in tried:
                    changed = current, acc
                    tried.add(changed)
                    current += arg
                else:
                    current, acc = changed
                    changed = None
            continue
        elif instruction == 'acc':
            acc += arg
        current += 1
    return acc


if __name__ == '__main__':
    print('acc (repeat):', day_8_1())
    print('acc (change):', day_8_2())
