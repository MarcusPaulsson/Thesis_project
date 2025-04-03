def is_stack_sortable(n, k, p):
    used = set(p)
    remaining = [i for i in range(1, n + 1) if i not in used]
    stack = []
    b = []
    
    idx = 0
    for i in range(k):
        while idx < len(remaining) and (not stack or stack[-1] < p[i]):
            stack.append(remaining[idx])
            idx += 1
        if stack and stack[-1] == p[i]:
            b.append(stack.pop())
        else:
            return -1
    
    while stack:
        b.append(stack.pop())
    
    if len(b) != n:
        return -1
    
    return p + b[len(p):]

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

result = is_stack_sortable(n, k, p)
if result == -1:
    print(-1)
else:
    remaining = [i for i in range(1, n + 1) if i not in result]
    remaining.reverse()  # To make it lexicographically maximal
    print(" ".join(map(str, result + remaining)))