from time import time

def time_func(func, n):
    print(f'Running {func.__name__}({n})')
    t0 = time()
    res = func(n)
    t1 = time()
    elapsed = round(t1 - t0, 8)
    print(f'Result: {res}, elapsed: {elapsed}')