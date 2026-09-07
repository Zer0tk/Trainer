from constants import DEFAULT_RETURN_INDEX_BASE

from typing import Any


def calculate_overdue_fine(name: Any, days_overdue: Any, fine_rate: Any) -> tuple[float, float] | None:
    """Calculates overdue fine and the return index. Includes safe handling of invalid input data with event logging.

    Args:
        name (Any): Film name.
        days_overdue (Any): Number of overdue days (must be castable to a float).
        fine_rate (Any): Fine rate for 1 day of overdue (must be castable to a float).

    Returns:
        tuple[float, float] | None: Tuple containing the total fine amount and the return index upon success. Otherwise (in the event of an error), it returns None.

    Raises:
        TypeError: If the data types don't support math operations.
        ValueError: If the number data is impossible to cast into float.
        ZeroDivisionError: If number of overdue days is 0.
    """

    total_fine = None
    return_index = None

    try:
        numeric_days = float(days_overdue)

        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{name}': {e}")
    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ]: Невозможно преобразовать дни в число для '{name}': {e}")
    except ZeroDivisionError as e:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ]: Возврат без просрочки для '{name}': {e}")
    finally:
        print("--- Проверка транзакции возврата завершена ---") ### Нахождение здесь вывода мешает совпадению фактических результатов с ожидаемыми, однако подчинено требованию реализации
        return (total_fine, return_index) if (total_fine and return_index) else None
