def is_stack_sortable(n, k, p):
    # Create a set for the elements already in p
    present = set(p)
    # Initialize the result array with the first k elements
    result = p[:]
    
    # Initialize the next number to be placed in the permutation
    next_num = n
    
    # Initialize a stack to simulate the stack operations
    stack = []
    
    # Iterate through the first k elements
    for i in range(k):
        # While the stack is not empty and the top of the stack is less than the next number
        while stack and stack[-1] < next_num:
            result.append(stack.pop())
        
        # If the current element is not the next number, we need to fill the stack
        if p[i] < next_num:
            # Push numbers onto the stack until we reach the current element
            while next_num > p[i]:
                if next_num not in present:
                    stack.append(next_num)
                next_num -= 1
        
        # If the current element is not the next number, it's impossible to sort
        if p[i] != next_num:
            return -1
        
        # Move to the next number
        next_num -= 1
    
    # After processing the first k elements, we need to empty the stack
    while stack:
        result.append(stack.pop())
    
    # Check if the result is a valid permutation
    if len(result) != n or len(set(result)) != n:
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