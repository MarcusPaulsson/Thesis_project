def fill_gifts(n, f):
    # Find the friends who want to give gifts (f_i != 0)
    givers = set(i + 1 for i in range(n) if f[i] != 0)
    # Find the friends who are not receiving gifts (f_i == 0)
    receivers = set(range(1, n + 1)) - givers

    # Fill in the unknown values
    for i in range(n):
        if f[i] == 0:
            # Find a receiver that is not the current friend (i + 1)
            for r in receivers:
                if r != i + 1:
                    f[i] = r
                    receivers.remove(r)
                    break

    return f

# Input reading
n = int(input())
f = list(map(int, input().split()))

# Fill the gifts and print the result
result = fill_gifts(n, f)
print(' '.join(map(str, result)))