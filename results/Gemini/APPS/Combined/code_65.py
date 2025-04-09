def solve():
    """
    Solves the Game 23 problem.

    Reads two integers n and m from input.
    Calculates the number of moves required to transform n to m by multiplying by 2 or 3.
    Prints the number of moves or -1 if it's impossible.
    """
    n, m = map(int, input().split())

    if n == m:
        print(0)
        return

    if m % n != 0:
        print(-1)
        return

    diff = m // n
    count = 0

    while diff % 2 == 0:
        diff //= 2
        count += 1

    while diff % 3 == 0:
        diff //= 3
        count += 1

    if diff != 1:
        print(-1)
    else:
        print(count)


solve()