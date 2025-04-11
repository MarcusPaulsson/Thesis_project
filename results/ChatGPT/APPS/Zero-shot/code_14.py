def is_stack_sortable(n, k, p):
    # Create a set of used elements
    used = set(p)
    # Create a list for the remaining elements
    remaining = [i for i in range(1, n + 1) if i not in used]
    
    # Initialize the result with the first k elements
    result = p[:]
    
    # Initialize a stack
    stack = []
    
    # The next number we need to push to the result
    next_needed = 1
    
    for i in range(k):
        # While we can pop from the stack to maintain sorted order
        while stack and stack[-1] == next_needed:
            result.append(stack.pop())
            next_needed += 1
        
        # If the current element is the next needed, add it to the result
        if p[i] == next_needed:
            result.append(p[i])
            next_needed += 1
        else:
            # Otherwise, we push the current element to the stack
            stack.append(p[i])
    
    # Now we need to process the remaining elements
    for num in sorted(remaining, reverse=True):
        while stack and stack[-1] == next_needed:
            result.append(stack.pop())
            next_needed += 1
        stack.append(num)
    
    # Finally, pop all remaining elements in the stack
    while stack and stack[-1] == next_needed:
        result.append(stack.pop())
        next_needed += 1
    
    # If we have used all numbers from 1 to n, we have a valid permutation
    if next_needed - 1 == n:
        return result
    else:
        return -1

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Get the result
result = is_stack_sortable(n, k, p)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))