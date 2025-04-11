def is_stack_sortable(n, k, p):
    # Create a set of used numbers from the first k elements
    used = set(p)
    
    # Create the remaining elements that need to be added to the permutation
    remaining = [i for i in range(1, n + 1) if i not in used]
    
    # Initialize the stack and the result array
    stack = []
    result = p[:]
    
    # We will iterate over the first k elements and simulate the stack operations
    for i in range(k):
        while stack and (not remaining or stack[-1] < remaining[-1]):
            result.append(stack.pop())
        stack.append(p[i])
    
    # Now we need to add the remaining elements in a way that keeps the stack sortable
    for num in reversed(remaining):
        while stack and stack[-1] < num:
            result.append(stack.pop())
        stack.append(num)
    
    # Finally, pop all remaining elements from the stack
    while stack:
        result.append(stack.pop())
    
    # Check if the result is stack-sortable
    if result == sorted(result):
        return result
    else:
        return -1

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