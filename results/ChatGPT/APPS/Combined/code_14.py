def is_stack_sortable(n, k, p):
    stack = []
    b = []
    remaining = set(range(1, n + 1)) - set(p)

    # Initialize the result array with the given first k elements
    result = list(p)

    # Process the given elements
    for i in range(k):
        while stack and (not remaining or stack[-1] > max(remaining)):
            b.append(stack.pop())
        stack.append(p[i])

    # Add remaining elements to the stack in descending order
    for next_elem in sorted(remaining, reverse=True):
        while stack and (not remaining or stack[-1] > max(remaining)):
            b.append(stack.pop())
        stack.append(next_elem)

    # Empty the stack into b
    while stack:
        b.append(stack.pop())

    # Check if b is sorted
    if b != sorted(b):
        return -1

    # Fill the result array with b
    result.extend(b)
    return result

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Get the result
result = is_stack_sortable(n, k, p)

# Output the result
if result == -1:
    print(result)
else:
    print(' '.join(map(str, result)))