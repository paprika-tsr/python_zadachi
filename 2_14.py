from contextlib import contextmanager


@contextmanager
def log_operation(filename, operation_name):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"START: {operation_name}\n")
    try:
        yield
    except Exception:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"ERROR: {operation_name}\n")
        raise
    else:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"END: {operation_name}\n")


with log_operation("operation.log", "Data processing"):
    result = 1 / 0
