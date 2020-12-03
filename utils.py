from typing import Callable, List, TypeVar, Any
import httplib2
from functools import wraps
from os.path import join
from env import COOKIE  # this should be your session cookie

T = TypeVar('T')
R = TypeVar('R')

ROOT = "https://adventofcode.com/2020/day/"
h = httplib2.Http(".cache")


def run(mapper: Callable[[str], T] = int):
    def decorator(f: Callable[[List[T], Any], R]) -> Callable[..., R]:
        day_num = f.__name__.split("_")[1]
        url = join(ROOT, day_num, "input")
        _, content = h.request(url, "GET", headers={"Cookie": COOKIE})
        content = content.decode().strip()

        @wraps(f)
        def wrapper(*args, **kwargs):
            data = list(map(mapper, content.split('\n')))
            return f(data, *args, **kwargs)
        return wrapper
    return decorator


def ident(x):
    return x
