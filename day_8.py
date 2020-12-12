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

# @test(parse_instruction, examples=examples)
@run(parse_instruction)
def day_8_2(instructions: List[Tuple[str, int]]) -> int:
    nops, jmps, visited, ip = [], [], [], 0
    # jmps = []
    # visited = []
    # ip = 0
    # for n, (instruction, _) in enumerate(instructions):
    #     if instruction == 'nop':
    #         nops.append(n)
    #     elif instruction == 'jmp':
    #         jmps.append(n)
    while ip not in visited:
        visited.append(ip)
        if instructions[ip][0] == 'jmp':
            jmps.append(ip)
            ip += instructions[ip][1]
            continue
        if instructions[ip][0] == 'nop':
            nops.append(ip)
            pass
        ip += 1

    for i in nops:
        ip = acc = 0
        visited = []
        while ip not in visited and ip < len(instructions):
            visited.append(ip)
            if ip == i or instructions[ip][0] == 'jmp':
                ip += instructions[ip][1]
                continue
            elif instructions[ip][0] == 'nop':
                ip += 1
            elif instructions[ip][0] == 'acc':
                acc += instructions[ip][1]
            ip += 1
        if ip >= len(instructions):
            return acc

    for i in jmps:
        ip = acc = 0
        visited = []
        while ip not in visited and ip < len(instructions):
            visited.append(ip)
            if ip == i or instructions[ip][0] == 'nop':
                pass
            elif ip == i or instructions[ip][0] == 'jmp':
                ip += instructions[ip][1]
                continue
            elif instructions[ip][0] == 'acc':
                acc += instructions[ip][1]
            ip += 1
        if ip >= len(instructions):
            return acc


if __name__ == '__main__':
    # print('acc (repeat):', day_8_1())
    print('acc (change):', day_8_2())
