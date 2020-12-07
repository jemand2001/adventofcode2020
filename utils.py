from typing import Callable, List, TypeVar, Any, Iterable
import httplib2
from functools import wraps
from os.path import join
from env import COOKIE  # this should be your session cookie

T = TypeVar('T')
R = TypeVar('R')

ROOT = "https://adventofcode.com/2020/day/"
h = httplib2.Http(".cache")


def run(mapper: Callable[[str], T] = int, sep: str = '\n'):
    def decorator(f: Callable[[List[T], Any], R]) -> Callable[..., R]:
        day_num = f.__name__.split("_")[1]
        url = join(ROOT, day_num, "input")
        _, content = h.request(url, "GET", headers={"Cookie": COOKIE})
        content = content.decode().strip()

        @wraps(f)
        def wrapper(*args, **kwargs):
            data = list(map(mapper, content.split(sep)))
            return f(data, *args, **kwargs)
        return wrapper
    return decorator


def test(mapper: Callable[[str], T] = int, sep: str = '\n', *, examples: Iterable[str] = ()):
    def decorator(f: Callable[[List[T], Any], R]) -> Callable[..., R]:
        @wraps(f)
        def wrapper(*args, **kwargs):
            return tuple(f(list(map(mapper, content.split(sep))), *args, **kwargs) for content in examples)
        return wrapper
    return decorator

def ident(x):
    return x

def part(idx: int):
    return lambda s: (s[:idx], s[idx:])

def split_at(sep):
    return lambda s: s.split(sep)
