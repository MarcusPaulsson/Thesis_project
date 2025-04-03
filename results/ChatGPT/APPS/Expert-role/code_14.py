def is_stack_sortable(n, k, p):
    # Create a set of used elements from the first k elements
    used = set(p)
    
    # Initialize the stack and the resulting permutation
    stack = []
    result = p[:]
    
    # The next possible largest number we can use in the result
    next_max = n
    
    for i in range(k):
        # Ensure that the stack is sorted correctly
        while stack and stack[-1] < result[i]:
            # Pop from stack if it maintains order
            result.append(stack.pop())
        
        # If the current element is less than the next max, we push elements to maintain order
        while next_max > 0 and (next_max in used or next_max > result[i]):
            stack.append(next_max)
            next_max -= 1
        
        # If the current element is not in stack and not larger than next_max, we have an issue
        if result[i] < next_max:
            return -1
    
    # Add remaining elements to the stack
    while next_max > 0:
        if next_max not in used:
            stack.append(next_max)
        next_max -= 1
    
    # Add remaining elements from stack to result
    while stack:
        result.append(stack.pop())
    
    return result

# Read input
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Get the result and print
result = is_stack_sortable(n, k, p)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))