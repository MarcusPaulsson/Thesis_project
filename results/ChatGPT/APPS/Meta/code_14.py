def is_stack_sortable(n, k, p):
    # Create a set for the used values and a stack
    used = set(p)
    stack = []
    result = p[:]
    
    # The next number to place into the permutation
    next_number = n
    
    # Traverse the given permutation
    for i in range(k):
        # While the stack has elements and the top of the stack is the next expected number
        while stack and stack[-1] == next_number:
            result.append(stack.pop())
            next_number -= 1
        
        # If the current number is less than the next_number, we cannot stack-sort
        if p[i] > next_number:
            return -1
        
        # Push the current number to the stack
        stack.append(p[i])
    
    # Now we need to fill the rest of the permutation
    while len(result) < n:
        while stack and stack[-1] == next_number:
            result.append(stack.pop())
            next_number -= 1
        
        # We can only add numbers that are not used yet
        while next_number in used:
            next_number -= 1
        
        if next_number <= 0:
            return -1
        
        result.append(next_number)
        used.add(next_number)
        next_number -= 1
    
    # Final check, if the stack can be emptied correctly
    while stack:
        if stack[-1] != next_number:
            return -1
        result.append(stack.pop())
        next_number -= 1
        
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