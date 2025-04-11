def fill_gift_givers(n, f):
    # Find the friends who have not been assigned a gift
    assigned = set(f) - {0}
    unassigned = [i for i in range(1, n + 1) if i not in assigned]
    zero_indices = [i for i in range(n) if f[i] == 0]

    # Create a result list initialized with the original values
    result = f[:]

    # Fill in the unassigned values
    for i in range(len(zero_indices)):
        # Assign the unassigned friend to the current zero index
        result[zero_indices[i]] = unassigned[i]

    # Ensure no one gives a gift to themselves
    for i in range(len(zero_indices)):
        if result[zero_indices[i]] == zero_indices[i] + 1:
            # Swap with the next unassigned if possible
            if i + 1 < len(zero_indices):
                result[zero_indices[i]], result[zero_indices[i + 1]] = result[zero_indices[i + 1]], result[zero_indices[i]]

    return result

# Input reading
n = int(input())
f = list(map(int, input().split()))

# Get the result
result = fill_gift_givers(n, f)

# Print the result
print(' '.join(map(str, result)))