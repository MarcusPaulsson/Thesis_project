def is_stack_sortable(n, k, p):
    used = set(p)
    remaining = [i for i in range(1, n + 1) if i not in used]
    
    # Create an empty stack
    stack = []
    b = []
    
    # Try to construct the lexicographically maximum permutation
    idx = 0
    for i in range(k):
        while idx < len(remaining) and (not stack or stack[-1] < p[i]):
            stack.append(remaining[idx])
            idx += 1
        # Now we can pop from the stack to form b
        if stack and stack[-1] == p[i]:
            b.append(stack.pop())
        else:
            # If we cannot match p[i], it's impossible
            return -1
    
    # Push remaining elements from remaining to stack
    while idx < len(remaining):
        stack.append(remaining[idx])
        idx += 1
    
    # Now, pop all elements from the stack to form b
    while stack:
        b.append(stack.pop())
    
    return p + b

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

result = is_stack_sortable(n, k, p)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))