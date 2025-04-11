def stack_sortable_permutation(n, k, p):
    # Create a set of used elements from the first k elements
    used = set(p)
    
    # Initialize the result permutation with the first k elements
    result = p[:]
    
    # Initialize the next available number to fill in the permutation
    next_available = n
    
    # Stack to simulate the stack operations
    stack = []
    
    # Iterate through the first k elements
    for i in range(k):
        # While the stack is not empty and the top of the stack is less than the next element
        while stack and stack[-1] < next_available:
            result.append(stack.pop())
        
        # If the current element is less than the next available, we cannot form a valid permutation
        if p[i] < next_available:
            return -1
        
        # Push the current element onto the stack
        stack.append(p[i])
        
        # Decrease the next available number
        next_available -= 1
    
    # Fill the remaining elements in the result
    while next_available > 0:
        if next_available not in used:
            result.append(next_available)
        next_available -= 1
    
    # Check if the result is stack-sortable
    stack = []
    b = []
    
    for num in result:
        stack.append(num)
        while stack and (not b or stack[-1] <= b[-1]):
            b.append(stack.pop())
    
    if len(b) != n:
        return -1
    
    return result

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Get the result
result = stack_sortable_permutation(n, k, p)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))