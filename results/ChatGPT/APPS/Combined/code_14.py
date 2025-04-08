def is_stack_sortable(permutation):
    stack = []
    b = []
    for num in permutation:
        stack.append(num)
        while stack and (not b or stack[-1] <= b[-1]):
            b.append(stack.pop())
    return b == sorted(permutation)

def restore_permutation(n, k, given):
    remaining = sorted(set(range(1, n + 1)) - set(given), reverse=True)

    # Check if the given part is stack-sortable
    if not is_stack_sortable(given):
        return -1

    result = given[:]
    stack = []

    for num in given:
        while remaining and (not stack or remaining[-1] >= stack[-1]):
            stack.append(remaining.pop())
        
        while stack and (not result or stack[-1] <= result[-1]):
            result.append(stack.pop())

    while stack:
        result.append(stack.pop())

    return result if len(result) == n else -1

# Read input
n, k = map(int, input().split())
given = list(map(int, input().split()))

# Get the result
result = restore_permutation(n, k, given)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))