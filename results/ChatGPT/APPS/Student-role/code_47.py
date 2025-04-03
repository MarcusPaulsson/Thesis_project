def max_strength(n, a):
    a.sort()
    max_strength = 0
    for i in range(n):
        if i % 2 == 0:
            max_strength += a[n - 1 - i]
        else:
            max_strength -= a[n - 1 - i]
    return max_strength

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    result = []
    result.append(max_strength(n, a))
    print(*result)