import concurrent.futures
import time


def run_with_execute_time(func):
    start_time = time.time()
    result = func()
    end_time = time.time()
    run_time = end_time - start_time
    return {'result': result, 'run_time_second': run_time}


def multi_processing(tasks: list, max_workers=4):
    results = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(run_with_execute_time, func=task) for task in tasks]
        for future in concurrent.futures.as_completed(futures):
            r = future.result()
            results.append(r)
        executor.shutdown()
    return results
