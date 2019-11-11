import time
from memory_profiler import memory_usage


def elapsed_milliseconds(func):

    def timer(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f'Elapsed: {runtime * 1000:.2f} msec')

    return timer


def allocated_memory(func):

    def tracker(*args, **kwargs):
        start = memory_usage(interval=0.00001, max_usage=True)
        func(*args, **kwargs)
        end = memory_usage(interval=0.00001, max_usage=True)
        usage = end - start
        print(f'Allocated: {usage:.2f} MiB')

    return tracker


def benchmark(func):
    @allocated_memory
    @elapsed_milliseconds
    def marker(*args, **kwargs):
        output_separator(func)
        value = func(*args, **kwargs)
        print(f'Result: {value}')

    return marker


def memory_king():
    return [1] * (10 ** 5)


def output_separator(func):
    function_name = func.__name__
    rule = '-' * len(function_name)
    print(f'\n{rule}')
    print(function_name)
    print(rule)

    return
