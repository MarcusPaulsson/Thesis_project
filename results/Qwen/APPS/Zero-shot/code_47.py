def max_beauty(n, x, a):
    if x == 1:
        return max([0] + [sum(a[i:j+1]) for i in range(n) for j in range(i, n)])
    elif x == -1:
        return max([0] + [sum(a[i:j+1]) for i in range(n) for j in range(i, n) if all(a[k] < 0 for k in range(i, j+1)])
    else:
        return max([0] + [sum(a[i:j+1]) * x for i in range(n) for j in range(i, n)])

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(max_beauty(n, x, a))