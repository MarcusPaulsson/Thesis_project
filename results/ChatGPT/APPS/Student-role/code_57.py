def fill_gifts(n, f):
    # Create a list to store the final gift assignments
    nf = f[:]
    
    # Find the friends who have not been assigned a gift
    unassigned = [i + 1 for i in range(n) if nf[i] == 0]
    
    # Find the friends who are already assigned gifts
    assigned = set(f) - {0}
    
    # Find the friends who can receive gifts (those not assigned)
    can_receive = [i + 1 for i in range(1, n + 1) if i not in assigned]
    
    # Fill the unassigned gifts
    for i in range(len(unassigned)):
        # Assign the gift to the next available friend
        nf[unassigned[i] - 1] = can_receive[i]
    
    # Ensure no one gives a gift to themselves
    for i in range(n):
        if nf[i] == i + 1:
            # Swap with the last unassigned friend
            nf[i], nf[unassigned[-1] - 1] = nf[unassigned[-1] - 1], nf[i]
            break
    
    return nf

# Input reading
n = int(input())
f = list(map(int, input().split()))

# Get the result and print it
result = fill_gifts(n, f)
print(' '.join(map(str, result)))