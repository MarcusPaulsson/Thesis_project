def solve():
    n, m = map(int, input().split())

    if n == m:
        print(0)
        return

    if m % n != 0:
        print(-1)
        return

    k = m // n

    count2 = 0
    count3 = 0

    while k % 2 == 0:
        k //= 2
        count2 += 1

    while k % 3 == 0:
        k //= 3
        count3 += 1

    if k != 1:
        print(-1)
        return

    print(count2 + count3)

solve()