n = int(input())
f = list(map(int, input().split()))

# Find the friends who have not been assigned gifts
assigned = set(f) - {0}
unassigned = [i for i in range(1, n + 1) if i not in assigned]

# Find the indices of friends who have not decided whom to give gifts to
zero_indices = [i for i in range(n) if f[i] == 0]

# Assign gifts to the friends who have not decided
for i in range(len(zero_indices)):
    f[zero_indices[i]] = unassigned[i]

# Print the result
print(' '.join(map(str, f)))