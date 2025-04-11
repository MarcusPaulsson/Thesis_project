def restore_stack_sortable_permutation(n, k, p):
    used = set(p)
    remaining = [i for i in range(1, n + 1) if i not in used]
    s = []
    result = p[:]
    
    for i in range(k):
        while s and (not remaining or s[-1] < remaining[-1]):
            result.append(s.pop())
        s.append(p[i])
    
    while s:
        result.append(s.pop())
    
    while remaining:
        if s and s[-1] < remaining[-1]:
            print(-1)
            return
        result.append(remaining.pop())
    
    print(" ".join(map(str, result)))

# Example usage:
# n, k = map(int, input().split())
# p = list(map(int, input().split()))
# restore_stack_sortable_permutation(n, k, p)