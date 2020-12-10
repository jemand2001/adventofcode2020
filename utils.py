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
    """the run decorator.
    :param mapper: a function applied to all elements of the input (usually lines)
    :param sep: the separator between elements of the input (usually \n)
    """
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
    """the test decorator.
    :param mapper: a function applied to all elements of the input (usually lines)
    :param sep: the separator between elements of the input (usually \n)
    :param examples: a collection of sample input strings
    """
    def decorator(f: Callable[[List[T], Any], R]) -> Callable[..., R]:
        @wraps(f)
        def wrapper(*args, **kwargs):
            return tuple(f(list(map(mapper, content.split(sep))), *args, **kwargs) for content in examples)
        return wrapper
    return decorator

def cached(f: Callable[..., R]) -> Callable[..., R]:
    calls = {}

    @wraps(f)
    def wrapper(*args, **kwargs):
        arguments = tuple([*args, *kwargs.items()])
        if arguments not in calls:
            calls[arguments] = f(*args, **kwargs)
        return calls[arguments]
    return wrapper

def ident(x):
    return x

def part(idx: int):
    return lambda s: (s[:idx], s[idx:])

def split_at(sep):
    return lambda s: tuple(s.split(sep))
