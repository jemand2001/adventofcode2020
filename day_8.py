from utils import run, split_at, test
from typing import List, Tuple

examples = ("""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""",)

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

@test(parse_instruction, examples=examples)
def day_8_2(instructions: List[Tuple[str, int]]) -> int:
    visited = []
    changed = []
    tried = set()
    current = 0
    acc = 0
    while current < len(instructions):
        visited.append(current)
        instruction, arg = instructions[current]
        print(instruction, arg)
        if instruction == 'jmp':
            if current + arg not in visited:
                if len(changed) == 0 and current not in tried:
                    changed.append((current, acc))
                    tried.add(current)
                    current += 1
                else:
                    current, acc = changed.pop()
                    # changed = None
                continue
            else:
                current += arg
        if instruction == 'nop':
            if current + 1 in visited and current + arg >= len(instructions):
                if len(changed) == 0 and current not in tried:
                    changed.append((current, acc))
                    tried.add(current)
                    current += arg
                else:
                    current, acc = changed.pop()
                    # changed = None
            current += 1
            continue
        elif instruction == 'acc':
            acc += arg
        current += 1
    return acc


if __name__ == '__main__':
    # print('acc (repeat):', day_8_1())
    print('acc (change):', day_8_2())
