def assign_gifts(n, f):
    result = f[:]  # Create a copy of the input list to store results
    givers = set(range(1, n + 1)) - set(f)  # Friends who want to give gifts (0 in f)
    receivers = [i + 1 for i in range(n) if result[i] == 0]  # Friends who need to assign gifts

    # Assign gifts to receivers
    for receiver in receivers:
        # Find a giver that is not the same as the receiver
        for giver in givers:
            if giver != receiver:
                result[receiver - 1] = giver  # Assign the gift
                givers.remove(giver)  # Remove the assigned giver from the pool
                break

    return result

# Example of usage
n = int(input())
f = list(map(int, input().split()))
result = assign_gifts(n, f)
print(' '.join(map(str, result)))