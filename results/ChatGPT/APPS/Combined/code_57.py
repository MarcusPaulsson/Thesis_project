def assign_gifts(n, f):
    # Identify givers and receivers
    givers = set(range(1, n + 1)) - set(f)  # Friends who have not been assigned a gift
    receivers = {gift for gift in f if gift != 0}  # Friends who are already assigned a gift

    # Prepare to fill in the zeros
    result = f[:]  # Copy the original list to result
    zero_indices = [i for i in range(n) if f[i] == 0]  # Indices of friends who have not chosen a gift

    # Assign gifts to friends with f_i = 0
    for i in zero_indices:
        for giver in givers:
            if giver != i + 1:  # Ensure the giver does not give to themselves
                result[i] = giver
                givers.remove(giver)  # Remove the giver from the available set
                receivers.add(giver)  # Add the giver to the receivers
                break

    return result

# Input reading
n = int(input())
f = list(map(int, input().split()))

# Get the result and print it
result = assign_gifts(n, f)
print(' '.join(map(str, result)))