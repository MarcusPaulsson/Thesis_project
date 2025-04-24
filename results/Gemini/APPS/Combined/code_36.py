def solve():
    n = int(input())

    if n == 0:
        print(0, 0)
        return

    l, r = 0, 10**9
    k = 0
    while l <= r:
        mid = (l + r) // 2
        if 3 * mid * (mid + 1) >= n:
            k = mid
            r = mid - 1
        else:
            l = mid + 1

    n -= 3 * k * (k - 1)
    side_length = 2 * k

    if n <= side_length // 2:
        print(side_length // 2 - n, 2 * n)
    elif n <= side_length:
        n -= side_length // 2
        print(side_length // 2 - 2 * n, side_length)
    elif n <= 3 * side_length // 2:
        n -= side_length
        print(-side_length // 2 - n, side_length - 2 * n)
    elif n <= 2 * side_length:
        n -= 3 * side_length // 2
        print(-side_length // 2 + n, -side_length)
    elif n <= 5 * side_length // 2:
        n -= 2 * side_length
        print(side_length // 2 + n, -side_length + 2 * n)
    else:
        n -= 5 * side_length // 2
        print(side_length // 2 - 2 * n, 0)

solve()