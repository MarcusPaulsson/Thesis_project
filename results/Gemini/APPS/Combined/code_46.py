def solve():
    n, m = map(int, input().split())
    count = 0
    for i in range(5):
        count += (n - i + 4) // 5 * ((m - (5 - i) + 4) // 5) if (n - i + 4) // 5 > 0 and ((m - (5 - i) + 4) // 5) > 0 else 0
    print(count)

solve()