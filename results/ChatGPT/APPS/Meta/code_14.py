def is_stack_sortable(permutation):
    stack = []
    b = []
    for num in permutation:
        while stack and (not b or stack[-1] <= b[-1]):
            b.append(stack.pop())
        stack.append(num)
    while stack:
        b.append(stack.pop())
    return b == sorted(b)

def restore_permutation(n, k, p):
    used = set(p)
    remaining = [i for i in range(1, n + 1) if i not in used]
    
    # Check if the given prefix can lead to a stack sortable array
    if not is_stack_sortable(p):
        return -1
    
    result = p[:]
    remaining.sort(reverse=True)  # To make it lexicographically maximal
    
    # Try to build the complete permutation
    stack = []
    index = 0
    
    for num in p:
        while index < len(remaining) and (not stack or stack[-1] <= num):
            stack.append(remaining[index])
            index += 1
        result.append(stack.pop())
    
    while stack:
        result.append(stack.pop())
    
    return result

n, k = map(int, input().split())
p = list(map(int, input().split()))

result = restore_permutation(n, k, p)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))