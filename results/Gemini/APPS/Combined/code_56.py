def remove_trailing_zeros(x: int) -> int:
    """Removes trailing zeros from an integer.

    Args:
        x: The integer to process.

    Returns:
        The integer with trailing zeros removed.
    """
    while x % 10 == 0:
        x //= 10
    return x


def reachable_count(start_number: int) -> int:
    """Counts the number of reachable numbers from a starting number using the given f(x) function.

    Args:
        start_number: The initial number.

    Returns:
        The number of distinct reachable numbers.
    """
    reachable = {start_number}
    current_number = start_number

    while True:
        current_number = remove_trailing_zeros(current_number + 1)
        if current_number in reachable:
            break
        reachable.add(current_number)

    return len(reachable)


if __name__ == "__main__":
    n = int(input())
    print(reachable_count(n))