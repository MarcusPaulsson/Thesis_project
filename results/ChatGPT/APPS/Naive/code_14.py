def is_stack_sortable(p):
    stack = []
    b = []
    for num in p:
        while stack and (not b or stack[-1] <= b[-1]):
            b.append(stack.pop())
        stack.append(num)
    while stack:
        b.append(stack.pop())
    return b == sorted(b)

def lexicographically_maximal_permutation(n, k, p):
    used = set(p)
    remaining = [i for i in range(1, n + 1) if i not in used]
    remaining.sort(reverse=True)

    result = p[:]  # Start with the given part of the permutation
    stack = []
    
    for num in p:
        while remaining and (not stack or stack[-1] <= num):
            stack.append(remaining.pop())
        stack.append(num)
    
    while stack:
        result.append(stack.pop())
    
    if is_stack_sortable(result):
        return result
    return -1

# Read input
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Generate and print the result
result = lexicographically_maximal_permutation(n, k, p)
if result == -1:
    print(result)
else:
    print(" ".join(map(str, result)))