def is_stack_sortable(n, k, p):
    # Create a set for the used numbers
    used = set(p)
    # Create a stack and the result array
    stack = []
    result = []
    
    # The next number we can use
    next_number = n
    
    # Iterate through the first k elements
    for i in range(k):
        while next_number > 0 and (next_number in used or (not stack or stack[-1] != next_number)):
            if next_number not in used:
                stack.append(next_number)
            next_number -= 1
        
        # Check if we can push the current element to the result
        if stack and stack[-1] == p[i]:
            result.append(stack.pop())
        else:
            return -1
    
    # Now we need to fill the rest of the result
    while next_number > 0:
        if next_number not in used:
            stack.append(next_number)
        next_number -= 1
    
    # Append remaining elements from the stack to the result
    while stack:
        result.append(stack.pop())
    
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