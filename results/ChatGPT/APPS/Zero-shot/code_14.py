def is_stack_sortable(n, k, p):
    remaining = set(range(1, n + 1)) - set(p)
    s = []
    b = []
    idx = 0

    for i in range(k):
        while s and (not remaining or s[-1] < min(remaining)):
            b.append(s.pop())
        if p[i] in remaining:
            remaining.remove(p[i])
            s.append(p[i])
        else:
            return -1

    while s and (not remaining or s[-1] < min(remaining)):
        b.append(s.pop())

    if s:
        return -1

    result = p[:]
    for num in sorted(remaining, reverse=True):
        result.append(num)

    return result

n, k = map(int, input().split())
p = list(map(int, input().split()))
result = is_stack_sortable(n, k, p)

if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))