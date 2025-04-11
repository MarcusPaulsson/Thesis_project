def min_instability(n, a):
    a.sort()
    # Remove the first element or the last element
    return min(a[-1] - a[1], a[-2] - a[0])

n = int(input())
a = list(map(int, input().split()))
print(min_instability(n, a))