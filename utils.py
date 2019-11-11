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
        print(f'Allocated: {end - start:.2f} MiB')

    return tracker


def benchmark(func):
    @allocated_memory
    @elapsed_milliseconds
    def marker(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f'Reulst: {value}')

    return marker


def memory_king():
    return [1] * (10 ** 5)
