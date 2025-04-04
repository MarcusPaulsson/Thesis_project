n = int(input())
f = list(map(int, input().split()))

# Find the friends who have not been assigned a recipient (f_i = 0)
unassigned = [i for i in range(n) if f[i] == 0]

# Ensure there are at least two unassigned friends
if len(unassigned) < 2:
    raise ValueError("There should be at least two unassigned friends.")

# Prepare a list for the final assignments
result = f[:]

# Assign unassigned friends to each other in a way that no one gives a gift to themselves
for i in range(len(unassigned)):
    recipient_index = (i + 1) % len(unassigned)  # This ensures a circular assignment
    result[unassigned[i]] = unassigned[recipient_index] + 1  # Adjusting for 1-based index

print(" ".join(map(str, result)))