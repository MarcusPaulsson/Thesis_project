def distribute_gifts(n, f):
    # Prepare a list for the final output
    nf = f[:]
    
    # Identify friends who want to give gifts to someone
    givers = set(i + 1 for i in range(n) if f[i] != 0)
    # Identify friends who can receive gifts (those with f[i] == 0)
    receivers = set(i + 1 for i in range(n) if f[i] == 0)

    # Friends who need to be filled in
    need_to_fill = list(receivers - givers)

    # Fill the unknown values
    idx = 0
    for i in range(n):
        if nf[i] == 0:
            # Find a suitable recipient that is not the current index + 1
            while need_to_fill[idx] == i + 1:
                idx += 1
            nf[i] = need_to_fill[idx]
            idx += 1

    print(" ".join(map(str, nf)))

# Input reading
n = int(input())
f = list(map(int, input().split()))
distribute_gifts(n, f)