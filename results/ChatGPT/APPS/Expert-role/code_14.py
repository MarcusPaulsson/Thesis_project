def is_stack_sortable(n, k, p):
    given_set = set(p)
    remaining = [i for i in range(1, n + 1) if i not in given_set]
    stack = []
    b = []
    
    for i in range(k):
        while stack and (not remaining or stack[-1] < remaining[-1]):
            b.append(stack.pop())
        stack.append(p[i])
    
    while stack:
        b.append(stack.pop())
    
    if b != sorted(b):
        return -1
    
    remaining.sort(reverse=True)
    result = p + remaining
    
    return result

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

result = is_stack_sortable(n, k, p)

if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))