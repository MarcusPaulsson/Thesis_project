def stack_sortable_permutation(n, k, p):
    used = set(p)
    remaining = [i for i in range(1, n + 1) if i not in used]
    s = []
    b = []
    
    for i in range(k):
        while s and (not remaining or s[-1] < remaining[-1]):
            b.append(s.pop())
        s.append(p[i])
    
    while remaining:
        while s and (not remaining or s[-1] < remaining[-1]):
            b.append(s.pop())
        if remaining:
            s.append(remaining.pop())
    
    while s:
        b.append(s.pop())
    
    if b == sorted(b):
        return p + sorted(remaining, reverse=True)
    else:
        return -1

n, k = map(int, input().split())
p = list(map(int, input().split()))
result = stack_sortable_permutation(n, k, p)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))