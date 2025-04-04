def gcd_sequence(n, k):
    if k > n:
        return -1
    if n == k:
        return [1] * k
    if k == 1:
        return [n]
    if k == 2:
        return [n // 2, n - n // 2]
    if k == 3:
        if n % 3 == 0:
            return [n // 3, n // 3 + 1, n // 3 + 2]
        elif n % 3 == 1:
            return [n // 3, n // 3 + 1, n // 3 + 2 - 1]
        else:
            return [n // 3, n // 3 + 1 - 1, n // 3 + 2]
    return -1

n, k = map(int, input().split())
result = gcd_sequence(n, k)
if result == -1:
    print(-1)
else:
    print(*result)