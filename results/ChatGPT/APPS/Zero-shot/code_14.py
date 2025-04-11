def is_stack_sortable(n, k, p):
    # Create a set for the given elements
    given_set = set(p)
    
    # Create the remaining elements
    remaining = [i for i in range(1, n + 1) if i not in given_set]
    
    # Initialize the result with the first k elements
    result = p[:]
    
    # Initialize a stack
    stack = []
    
    # We will iterate through the given elements
    for i in range(k):
        # If the stack is not empty and the top of the stack is less than the next element
        while stack and stack[-1] < result[i]:
            result.append(stack.pop())
        
        # Push the current element onto the stack
        stack.append(result[i])
    
    # Now we need to add the remaining elements in a way that keeps the stack sortable
    for num in sorted(remaining, reverse=True):
        while stack and stack[-1] < num:
            result.append(stack.pop())
        stack.append(num)
    
    # Finally, pop all remaining elements from the stack
    while stack:
        result.append(stack.pop())
    
    # Check if the result is a valid permutation
    if len(result) != n or len(set(result)) != n:
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