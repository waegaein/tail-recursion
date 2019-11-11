import sys
from typing import Optional

from utils import benchmark, memory_king
from tail import tail_recursive, recurse


@benchmark
def fibonacci_plain_recursive(n: int):
    def _fibonacci_plain_recursion(n: int):
        a = memory_king()

        if n < 2:
            return 1
        else:
            return _fibonacci_plain_recursion(n - 1) + _fibonacci_plain_recursion(n - 2)

    return _fibonacci_plain_recursion(n)


@benchmark
def fibonacci_iterative(n: int):
    a = memory_king()

    if n < 2:
        return 1

    current = 1
    previous = 1

    for i in range(2, n + 1):
        temp = current
        current += previous
        previous = temp

    return current


@benchmark
def fibonacci_tail_recursive(n: int):
    @tail_recursive
    def _fibonacci_tail_recursive(n: int, before: Optional[int] = 1, two_before: Optional[int] = 1):
        a = memory_king()

        if n == 0:
            return two_before
        elif n == 1:
            return before
        else:
            return recurse(n - 1, before + two_before, before)

    return _fibonacci_tail_recursive(n)


def demonstrate(method: int, n: int):
    if method == 0:
        fibonacci_plain_recursive(n)
    elif method == 1:
        fibonacci_iterative(n)
    elif method == 2:
        fibonacci_tail_recursive(n)
    else:
        print(f'method {method} is not defined')

    return


if __name__ == '__main__':
    arg_method = int(sys.argv[1])
    arg_n = int(sys.argv[2])

    demonstrate(arg_method, arg_n)
