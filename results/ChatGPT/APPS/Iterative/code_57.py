def fill_gifts(n, f):
    assigned = set(fi for fi in f if fi != 0)
    unassigned = [i for i in range(1, n + 1) if i not in assigned]
    zero_indices = [i for i in range(n) if f[i] == 0]

    for i in range(len(zero_indices)):
        friend_index = zero_indices[i]
        gift_index = unassigned[i]

        # Ensure the gift is not assigned to the friend themselves
        if gift_index == friend_index + 1:
            # Swap with the next unassigned friend if possible
            if i + 1 < len(unassigned):
                unassigned[i], unassigned[i + 1] = unassigned[i + 1], unassigned[i]

        f[friend_index] = unassigned[i]

    return f

# Input reading
n = int(input())
f = list(map(int, input().split()))

# Fill the gifts and print the result
result = fill_gifts(n, f)
print(' '.join(map(str, result)))