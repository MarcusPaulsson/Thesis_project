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
    Solve the chocolate maximization problem.
    """
    n, a, b, p, q = map(int, input().split())

    red_count = n // a
    blue_count = n // b
    both_count = n // lcm(a, b)

    red_only = red_count - both_count
    blue_only = blue_count - both_count

    total_chocolates = 0

    if p > q:
        total_chocolates += red_only * p
        total_chocolates += both_count * p
        total_chocolates += blue_only * q
    else:
        total_chocolates += red_only * p
        total_chocolates += both_count * q
        total_chocolates += blue_only * q

    print(total_chocolates)

if __name__ == "__main__":
    solve()