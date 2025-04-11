def stack_sortable_permutation(n, k, p):
    # Initialize the set of used numbers and the stack
    used = set(p)
    stack = []
    result = p[:]
    
    # The next number to add to the permutation
    next_num = n
    
    # Iterate over the first k elements
    for i in range(k):
        # While we can push numbers to the stack
        while next_num > 0 and next_num not in used:
            stack.append(next_num)
            next_num -= 1
        
        # If the stack is not empty and the top of the stack is greater than the current element
        while stack and stack[-1] > result[i]:
            result.append(stack.pop())
    
    # After processing the first k elements, we need to fill the rest of the permutation
    while next_num > 0:
        if next_num not in used:
            stack.append(next_num)
        next_num -= 1
    
    # Now pop all remaining elements from the stack
    while stack:
        result.append(stack.pop())
    
    # Check if the result is stack-sortable
    if len(result) != n:
        return -1
    
    # Check if the result is valid
    if len(set(result)) != n or sorted(result) != list(range(1, n + 1)):
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