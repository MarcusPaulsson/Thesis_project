n = int(input())
f = list(map(int, input().split()))

# Find the friends who have not chosen anyone (f_i = 0)
unknown_indices = [i for i in range(n) if f[i] == 0]
chosen_friends = set(f) - {0}

# Find the friends who are not chosen by anyone
all_friends = set(range(1, n + 1))
not_chosen_friends = list(all_friends - chosen_friends)

# Assign the not chosen friends to the unknown indices
for i in range(len(unknown_indices)):
    f[unknown_indices[i]] = not_chosen_friends[i]

# Print the result
print(' '.join(map(str, f)))