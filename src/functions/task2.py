from constants import PERFORMANCE_LOG_PREFIX, TIME_DECIMALS

from typing import Callable, Any
from time import perf_counter


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """A decorator for logging function execution time. Measures the exec. time and outputs the results to the console.

    Args:
        func (Callable[..., Any]): Decorated function.

    Returns:
        Callable[..., Any]: Wrapped function that returns the result of the original one.
    """
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {round((end - start), TIME_DECIMALS)} сек.")
        return result
    return wrapper


@performance_logger
def get_sorted_report(dicts: list[dict[str, str|float]]) -> list[dict[str, str|float]]:
    """Sorts the list of reports by total sales in descending order.

    Args:
        dicts (list[dict[str, str | float]]): List of dictionaries containing report data with key 'total_sales'.

    Returns:
        list[dict[str, str | float]]: New sorted list of reports.
    """
    return sorted(dicts, key=lambda d: d["total_sales"], reverse=True)
