def min_D(n, a):
    a.sort()
    mid = a[n//2]
    D = float('inf')
    for i in range(n):
        D = min(D, max(mid - a[i], a[i] - mid))
    if D == float('inf'):
        return -1
    return D

n = int(input())
a = list(map(int, input().split()))
print(min_D(n, a))