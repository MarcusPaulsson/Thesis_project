def is_stack_sortable_and_restore(n, k, p):
    # Create a set for quick lookup of the first k elements
    used = set(p)
    # Initialize the result with the first k elements
    result = p[:]
    
    # The next value we can use to fill the remaining array
    next_value = n
    
    # We will use a stack to keep track of the order of elements
    stack = []
    
    # Check the conditions for stack sortability
    for i in range(k):
        # Ensure that the stack is always non-decreasing
        while stack and stack[-1] < result[i]:
            stack.pop()
        
        # If the top of the stack is greater than the current element,
        # it means we can't place the current element in a non-decreasing order
        if stack and stack[-1] > result[i]:
            return -1
        
        # Push the next available values into the stack until we reach the current element
        while next_value > 0 and next_value > result[i]:
            if next_value not in used:
                stack.append(next_value)
            next_value -= 1
    
    # Now we have filled the stack, we need to fill in the remaining values
    while next_value > 0:
        if next_value not in used:
            stack.append(next_value)
        next_value -= 1
    
    # Now we can append the remaining values from the stack
    while stack:
        if stack[-1] < result[-1] if result else float('inf'):
            return -1
        result.append(stack.pop())
    
    return result

# Read input
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Get the result
result = is_stack_sortable_and_restore(n, k, p)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))