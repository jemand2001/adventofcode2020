from utils import run, test
from typing import List, Tuple

Command = Tuple[str, int]
examples = ("""F10
N3
F7
R90
F11""",)

transform = {
    'N': complex(0, 1),
    'S': complex(0, -1),
    'E': complex(1, 0),
    'W': complex(-1, 0)
}


def parse_command(line: str) -> Command:
    return line[0], int(line[1:])

@run(parse_command)
def day_12_1(commands: List[Command]):
    pos = complex(0, 0)
    direction = complex(0, 1)
    for cmd, value in commands:
        if cmd in transform:
            pos += transform[cmd] * value
        elif cmd == 'L':
            direction *= complex(0, 1) ** (value // 90)
        elif cmd == 'R':
            direction *= complex(0, 1) ** (3 * value // 90)
        elif cmd == 'F':
            pos += direction * value
    return int(abs(pos.imag) + abs(pos.real))

# @test(parse_command, examples=examples)
@run(parse_command)
def day_12_2(commands: List[Command]):
    ship = complex(0, 0)
    waypoint = complex(10, 1)
    for cmd, value in commands:
        if cmd in transform:
            waypoint += transform[cmd] * value
        elif cmd == 'L':
            waypoint *= complex(0, 1) ** (value // 90)
        elif cmd == 'R':
            waypoint *= complex(0, 1) ** (3 * value // 90)
        elif cmd == 'F':
            ship += waypoint * value
    return int(abs(ship.imag) + abs(ship.real))


if __name__ == '__main__':
    print('end position (ship):', day_12_1())
    print('end position (waypoint):', day_12_2())
