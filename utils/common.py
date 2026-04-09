import time


def run_time(partial_func):
    start_time = time.time()
    result = partial_func()
    end_time = time.time()
    print(f'Execution time: {end_time - start_time} seconds')
    return result
