def solve():
    n = int(input())
    a = list(map(int, input().split()))

    results = []
    for k in range(1, n + 1):
        amazing_number = -1
        
        candidates = set()
        for i in range(n - k + 1):
            subsegment = a[i:i+k]
            if i == 0:
                candidates = set(subsegment)
            else:
                candidates = candidates.intersection(set(subsegment))
        
        if candidates:
            amazing_number = min(candidates)

        results.append(amazing_number)

    print(*results)

t = int(input())
for _ in range(t):
    solve()