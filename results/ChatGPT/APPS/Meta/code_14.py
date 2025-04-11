def is_stack_sortable(n, k, p):
    # Create a set of used elements from the first k elements
    used = set(p)
    # The remaining elements that need to be added to the permutation
    remaining = [i for i in range(1, n + 1) if i not in used]
    
    # Initialize the result with the first k elements
    result = p[:]
    
    # Initialize a stack
    stack = []
    
    # The next number we expect to append to the result
    next_expected = 1
    
    # Iterate through the first k elements
    for i in range(k):
        while stack and stack[-1] == next_expected:
            result.append(stack.pop())
            next_expected += 1
        
        # If the current element is not the expected one
        if p[i] != next_expected:
            # Push the current element onto the stack
            stack.append(p[i])
        else:
            # If it is the expected one, append it to the result
            result.append(p[i])
            next_expected += 1
    
    # Now we need to process the remaining elements
    for num in sorted(remaining, reverse=True):
        while stack and stack[-1] == next_expected:
            result.append(stack.pop())
            next_expected += 1
        stack.append(num)
    
    # Finally, empty the stack if possible
    while stack and stack[-1] == next_expected:
        result.append(stack.pop())
        next_expected += 1
    
    # Check if we have added all numbers from 1 to n
    if next_expected - 1 == n:
        print(" ".join(map(str, result)))
    else:
        print(-1)

# Example usage
n, k = map(int, input().split())
p = list(map(int, input().split()))
is_stack_sortable(n, k, p)