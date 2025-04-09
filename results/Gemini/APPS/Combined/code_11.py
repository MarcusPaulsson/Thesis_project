def gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Calculates the least common multiple (LCM) of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The least common multiple of a and b.
    """
    return (a * b) // gcd(a, b)


def solve():
    """
    Reads input, calculates the maximum number of chocolates Joty can get, and prints the result.
    """
    n, a, b, p, q = map(int, input().split())

    count_a = n // a
    count_b = n // b
    count_lcm = n // lcm(a, b)

    chocolates = count_a * p + count_b * q

    if p > q:
        chocolates -= count_lcm * q
    else:
        chocolates -= count_lcm * p

    print(chocolates)


if __name__ == "__main__":
    solve()