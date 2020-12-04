from utils import run, ident
from typing import List, Mapping


@run(ident)
def day_4_1(entries: List[str]):
    entries: List[str] = '\n'.join(entries).split('\n\n')
    entries_d: List[Mapping[str, str]] = []
    for e in entries:
        entries_d.append(parse(e))
    return sum(all(field in entry for field in REQUIRED) for entry in entries_d)


REQUIRED = (
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid',
)

EYE_COLORS = (
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth',
)

heights = {'cm': (150, 194), 'in': (59, 77)}


def parse(line: str) -> Mapping[str, str]:
    entry = {}
    for el in line.split():
        k, v = el.split(':')
        entry[k] = v
    return entry


def is_valid(entry: Mapping[str, str]) -> bool:
    try:
        suffix = entry['hgt'][-2:]
        height = int(entry['hgt'][:-2])
        height_valid = (
                suffix in ('in', 'cm') and
                height in range(*heights[suffix])
        )
        return (
                1920 <= int(entry['byr']) <= 2002 and
                2010 <= int(entry['iyr']) <= 2020 and
                2020 <= int(entry['eyr']) <= 2030 and
                height_valid and
                (hcl := entry['hcl'])[0] == '#' and
                len(hcl) == 7 and
                int(hcl[1:], base=16) >= 0 and
                entry['ecl'] in EYE_COLORS and
                len(entry['pid']) == 9
        )
    except KeyError:
        return False
    except ValueError:
        return False


@run(ident)
def day_4_2(lines: List[str]):
    entries = [parse(e) for e in '\n'.join(lines).split('\n\n')]
    return sum(is_valid(entry) for entry in entries)


if __name__ == '__main__':
    print(day_4_1())
    print(day_4_2())
