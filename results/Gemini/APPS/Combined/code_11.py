def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

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
    Calculate the least common multiple (LCM) of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The least common multiple of a and b.
    """
    return (a * b) // gcd(a, b)

def solve():
    """
    Solve the problem of maximizing the number of chocolates Joty can get by painting tiles Red or Blue.

    Reads input, calculates the number of tiles divisible by a and b, and determines the optimal
    painting strategy to maximize chocolate earnings. Prints the maximum number of chocolates.
    """
    n, a, b, p, q = map(int, input().split())

    red_count = n // a
    blue_count = n // b
    both_count = n // lcm(a, b)

    red_only = red_count - both_count
    blue_only = blue_count - both_count

    total_chocolates = red_only * p + blue_only * q

    if p > q:
        total_chocolates += both_count * p
    else:
        total_chocolates += both_count * q

    print(total_chocolates)

if __name__ == "__main__":
    solve()