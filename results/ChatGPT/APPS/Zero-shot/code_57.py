def fill_gifts(n, f):
    # Identify givers and takers
    givers = set(range(1, n + 1)) - set(filter(lambda x: x != 0, f))
    takers = set(filter(lambda x: x != 0, f))
    
    # Find the friends who do not have a recipient (f_i = 0)
    zero_indices = [i for i in range(n) if f[i] == 0]
    
    # Prepare a list for the final output
    nf = f[:]
    
    # Assign gifts to friends who have f_i = 0
    for i in zero_indices:
        # Find a suitable gift recipient
        for recipient in givers:
            if recipient not in takers and recipient != (i + 1):
                nf[i] = recipient
                givers.remove(recipient)
                takers.add(recipient)
                break

    return nf

# Input reading
n = int(input().strip())
f = list(map(int, input().strip().split()))

# Fill in the gifts
result = fill_gifts(n, f)

# Output the result
print(' '.join(map(str, result)))