def is_stack_sortable(n, k, p):
    # Create a set of used numbers from the first k elements
    used = set(p)
    # Create a list of remaining numbers that need to be filled
    remaining = [i for i in range(1, n + 1) if i not in used]
    
    # Initialize the result array with the first k elements
    result = p[:]
    
    # We will use a stack to simulate the operations
    stack = []
    
    # Pointer for remaining elements
    remaining_pointer = 0
    
    # Simulate the process to build the stack-sortable permutation
    for i in range(k):
        # Push elements onto the stack until we reach a point where we can pop
        while (remaining_pointer < len(remaining) and (not stack or remaining[remaining_pointer] > result[i])):
            stack.append(remaining[remaining_pointer])
            remaining_pointer += 1
        
        # If we can pop from the stack, do it
        if stack and (not result or stack[-1] < result[i]):
            print(-1)
            return
        
        # Pop from the stack to the result if it's valid
        if stack and stack[-1] == result[i]:
            stack.pop()
    
    # Now we need to add the remaining elements in a way that keeps it sorted
    while remaining_pointer < len(remaining):
        stack.append(remaining[remaining_pointer])
        remaining_pointer += 1
    
    # Finalizing the result
    while stack:
        result.append(stack.pop())
    
    print(" ".join(map(str, result)))

# Read input
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Call the function to determine the stack-sortable permutation
is_stack_sortable(n, k, p)