def restore_stack_sortable_permutation(n, k, p):
    # Create a set of used numbers from the first k elements
    used = set(p)
    
    # Create the remaining numbers that need to be filled in the permutation
    remaining = [i for i in range(1, n + 1) if i not in used]
    
    # Initialize the result with the first k elements
    result = p[:]
    
    # Initialize a stack to simulate the stack operations
    stack = []
    
    # The next number we need to push from remaining
    next_remaining_index = 0
    
    # Iterate over the first k elements to check stack-sortability
    for i in range(k):
        # While we can push from remaining and the top of the stack is less than the next needed
        while (next_remaining_index < len(remaining) and 
               (not stack or stack[-1] > p[i])):
            stack.append(remaining[next_remaining_index])
            next_remaining_index += 1
        
        # If the top of the stack is the current element, pop it
        if stack and stack[-1] == p[i]:
            stack.pop()
        else:
            # If we can't match the current element, it's not stack-sortable
            return -1
    
    # Now we need to fill the rest of the result with remaining elements
    while next_remaining_index < len(remaining):
        stack.append(remaining[next_remaining_index])
        next_remaining_index += 1
    
    # Pop all remaining elements from the stack to the result
    while stack:
        result.append(stack.pop())
    
    return result

# Read input
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Get the result
result = restore_stack_sortable_permutation(n, k, p)

# Print the result
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))