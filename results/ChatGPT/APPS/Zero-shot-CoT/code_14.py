def is_stack_sortable(n, k, p):
    # Create a set of used elements
    used = set(p)
    # Create a stack and the result array
    s = []
    b = []
    # Pointer for the next element to be added to b
    next_needed = 1
    
    # Process the first k elements
    for i in range(k):
        # While we can pop from the stack to b
        while s and s[-1] == next_needed:
            b.append(s.pop())
            next_needed += 1
        # Push current element onto the stack
        s.append(p[i])
    
    # Now we need to fill the remaining elements in a way that keeps it stack-sortable
    remaining = []
    for i in range(1, n + 1):
        if i not in used:
            remaining.append(i)
    
    # Fill remaining elements in reverse order to maximize lexicographical order
    remaining.reverse()
    
    # Add remaining elements
    for elem in remaining:
        while s and s[-1] == next_needed:
            b.append(s.pop())
            next_needed += 1
        s.append(elem)

    # Final pop from the stack
    while s and s[-1] == next_needed:
        b.append(s.pop())
        next_needed += 1
    
    # If we have added all numbers in order 1 to n
    if next_needed - 1 == n:
        return p + remaining
    else:
        return -1

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

result = is_stack_sortable(n, k, p)
if result == -1:
    print(result)
else:
    print(" ".join(map(str, result)))