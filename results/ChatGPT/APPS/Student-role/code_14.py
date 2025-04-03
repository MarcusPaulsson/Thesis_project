def is_stack_sortable(n, k, p):
    # Initialize the set of remaining elements
    remaining = set(range(1, n + 1)) - set(p)
    stack = []
    result = p[:]
    
    # Process the first k elements
    for num in p:
        while stack and stack[-1] < num:
            # If the top of the stack is less than the current number, we cannot continue
            return -1
        stack.append(num)
    
    # Fill in the remaining elements in reverse order to achieve lexicographical maximality
    for num in sorted(remaining, reverse=True):
        while stack and stack[-1] < num:
            result.append(stack.pop())
        stack.append(num)
    
    # Empty the stack to get the final result
    while stack:
        result.append(stack.pop())
    
    return result

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Get the result
result = is_stack_sortable(n, k, p)

# Output the result
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))