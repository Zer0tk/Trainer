from constants import MAX_RENTAL_BATCH_LIMIT


def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """Calculates the cost of a batch, applying the discount and checking whether the internal auto-approval limit is exceeded.

    Args:
        quantity (int): Number of discs per batch.
        rental_rate (float): Rental cost per disc.
        discount (float, optional): Discount amount as a fraction. Defaults to 0.0.

    Returns:
        tuple[float, bool]: Tuple containing the final sum (rounded to 2 decimals) and a flag indicating whether the auto-approval limit has been exceeded.
    """

    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return final_sum, is_limit_exceeded
