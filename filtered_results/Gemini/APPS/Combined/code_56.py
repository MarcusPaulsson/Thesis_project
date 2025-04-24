def f(x):
    """
    Applies the function f(x) as described in the problem statement.

    Args:
        x: An integer.

    Returns:
        The result of applying f(x) to x.
    """
    x += 1
    while x % 10 == 0:
        x //= 10
    return x


def solve():
    """
    Reads an integer n from input and calculates the number of reachable
    numbers from n using the function f(x).  Prints the count of reachable numbers.
    """
    n = int(input())
    reachable = set()
    current = n
    while current not in reachable:
        reachable.add(current)
        current = f(current)
    print(len(reachable))


if __name__ == "__main__":
    solve()