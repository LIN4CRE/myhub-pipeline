"""Core pipeline runner."""
import time


def run_stage(name: str, fn, *args, **kwargs):
    """Run a pipeline stage, return (result, duration_s)."""
    t0 = time.perf_counter()
    result = fn(*args, **kwargs)
    return result, round(time.perf_counter() - t0, 4)
