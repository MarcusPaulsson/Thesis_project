def is_stack_sortable(n, k, p):
    # Create a set of used elements from the first k elements
    used = set(p)
    # Initialize the result array with the first k elements
    result = p[:]
    
    # The next available number to use in the permutation
    next_available = n
    
    # A stack to simulate the stack operations
    stack = []
    
    # Iterate through the first k elements
    for i in range(k):
        # Push elements onto the stack until we can pop
        while next_available > 0 and (len(stack) == 0 or stack[-1] < p[i]):
            if next_available not in used:
                stack.append(next_available)
            next_available -= 1
        
        # If the stack's top is not equal to the current element, it's not sortable
        if len(stack) > 0 and stack[-1] == p[i]:
            stack.pop()
        elif len(stack) > 0 and stack[-1] > p[i]:
            return -1
    
    # Fill the remaining elements in the result
    while next_available > 0:
        if next_available not in used:
            result.append(next_available)
        next_available -= 1
    
    # Now we need to ensure the result is stack-sortable
    stack = []
    for num in result:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    
    # If the stack is not empty, we can check if we can pop all elements
    if len(stack) != len(result):
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