import time
from contextlib import contextmanager


class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.perf_counter()
        execution_time = end_time - self.start_time
        print(f"Время выполнения блока (класс): {execution_time:.6f} сек.")
        return False


with Timer():
    time.sleep(1)




@contextmanager
def timer_manager():
    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Время выполнения блока (contextlib): {execution_time:.6f} сек.")


with timer_manager():
    time.sleep(1)
