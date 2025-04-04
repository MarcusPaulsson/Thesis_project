def min_instability(n, a):
    a.sort()
    return min(a[i+1] - a[0] for i in range(n-1)) if n > 2 else 0

n = int(input())
a = list(map(int, input().split()))
print(min_instability(n, a))