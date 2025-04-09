def solve():
    n, m = map(int, input().split())
    count = 0
    for rem in range(1, 6):
        count += (n + 5 - rem) // 5 * ((m + rem - 1) // 5)
    print(count)

solve()