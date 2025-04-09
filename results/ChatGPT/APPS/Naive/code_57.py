def fill_gifts(n, f):
    givers = []
    receivers = set(range(1, n + 1))

    # Identify the friends who have specific targets and those that do not
    for i in range(n):
        if f[i] == 0:
            givers.append(i + 1)  # Store the 1-based index of friends who don't know
        else:
            receivers.discard(f[i])  # Remove the known receivers from the set

    # Now 'givers' contains friends that need to assign gifts
    # 'receivers' contains friends who can be assigned gifts
    receivers = list(receivers)

    # Fill in the gifts for those who had 0
    for i in range(len(givers)):
        giver = givers[i]
        receiver = receivers[i]
        f[giver - 1] = receiver  # Assign the gift

    return f

# Read input
n = int(input())
f = list(map(int, input().split()))

# Fill the gift assignments
result = fill_gifts(n, f)

# Print the result
print(" ".join(map(str, result)))