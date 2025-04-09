def fill_gifts(n, f):
    # Determine the set of givers and receivers
    givers = set(range(1, n + 1)) - set(f[i] for i in range(n) if f[i] != 0)
    receivers = [i + 1 for i in range(n) if f[i] == 0]

    # Create a mapping of known gift givers
    gift_map = {i + 1: f[i] for i in range(n) if f[i] != 0}

    # Fill in the undecided gifts
    undecided_givers = list(givers)
    idx = 0

    for i in range(n):
        if f[i] == 0:
            # Find a receiver who is not the current giver
            while idx < len(undecided_givers) and undecided_givers[idx] == (i + 1):
                idx += 1
                
            if idx < len(undecided_givers):
                f[i] = undecided_givers[idx]
                idx += 1
            
    return f

# Input reading
n = int(input())
f = list(map(int, input().split()))

# Fill gifts and output the result
result = fill_gifts(n, f)
print(" ".join(map(str, result)))