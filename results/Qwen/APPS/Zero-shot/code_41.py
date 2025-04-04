def nearest_zero(n, a):
    d = [0] * n
    last_zero = -1
    for i in range(n):
        if a[i] == 0:
            last_zero = i
        elif last_zero != -1:
            d[i] = min(d[i], i - last_zero)
    last_zero = n
    for i in range(n-1, -1, -1):
        if a[i] == 0:
            last_zero = i
        else:
            d[i] = min(d[i], last_zero - i)
    return d

n = int(input())
a = list(map(int, input().split()))
print(*nearest_zero(n, a))