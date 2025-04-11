def stack_sortable_permutation(n, k, p):
    if k == n:
        return -1
    
    remaining = list(range(k + 1, n + 1))
    remaining.sort(reverse=True)
    
    stack = []
    b = []
    
    for i in range(k):
        if p[i] > remaining[-1]:
            return -1
        while remaining and remaining[-1] <= p[i]:
            stack.append(remaining.pop())
        b.append(p[i])
    
    while remaining:
        stack.append(remaining.pop())
    
    while stack:
        b.append(stack.pop())
    
    return b

n, k = map(int, input().split())
p = list(map(int, input().split()))
result = stack_sortable_permutation(n, k, p)

if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))