def solve():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))

    min_shows = float('inf')

    for i in range(n - d + 1):
        segment = a[i:i+d]
        unique_shows = len(set(segment))
        min_shows = min(min_shows, unique_shows)

    print(min_shows)

t = int(input())
for _ in range(t):
    solve()