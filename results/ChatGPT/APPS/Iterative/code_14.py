def is_stack_sortable(n, k, p):
    # Create a set of used elements
    used = set(p)
    # Create a list for the remaining elements
    remaining = [i for i in range(1, n + 1) if i not in used]
    
    # Initialize the stack and the result array
    stack = []
    result = []
    
    # Iterate through the first k elements
    for i in range(k):
        # While stack is not empty and the top of the stack is less than the next element in p
        while stack and stack[-1] < p[i]:
            result.append(stack.pop())
        # Push the current element onto the stack
        stack.append(p[i])
    
    # Now we need to add the remaining elements in a way that keeps the result stack-sortable
    for num in sorted(remaining, reverse=True):
        while stack and stack[-1] < num:
            result.append(stack.pop())
        stack.append(num)
    
    # Empty the stack
    while stack:
        result.append(stack.pop())
    
    # Check if the result is a valid permutation
    if len(result) != n or sorted(result) != list(range(1, n + 1)):
        return -1
    
    return result

# Read input
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Get the result
result = is_stack_sortable(n, k, p)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))