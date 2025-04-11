def fill_gift_values(n, f):
    # Create a list to store the final gift assignments
    nf = f[:]
    
    # Find the friends who have not been assigned a gift
    unassigned = []
    for i in range(n):
        if nf[i] == 0:
            unassigned.append(i + 1)  # Store 1-based index

    # Find the friends who are already assigned gifts
    assigned = set(f) - {0}

    # Find the friends who are not assigned any gift
    not_assigned = [i for i in range(1, n + 1) if i not in assigned]

    # Assign gifts to the unassigned friends
    for i in range(len(unassigned)):
        # Assign the next available friend to give a gift to
        nf[unassigned[i] - 1] = not_assigned[i]

    return nf

# Read input
n = int(input())
f = list(map(int, input().split()))

# Get the result
result = fill_gift_values(n, f)

# Print the result
print(' '.join(map(str, result)))