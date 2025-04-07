n = int(input())
f = list(map(int, input().split()))

# Track friends who have not yet given a gift and who are supposed to receive gifts
unknown_indices = []
gifted = set()

for i in range(n):
    if f[i] == 0:
        unknown_indices.append(i)  # Store 0-based index
    else:
        gifted.add(f[i])

# Find friends who are not in the gifted set
not_gifted = [i for i in range(1, n + 1) if i not in gifted]

# Fill in the unknown gift receivers
for i in range(len(unknown_indices)):
    # Assign gifts while ensuring no one gives a gift to themselves
    current_unknown_index = unknown_indices[i]
    if (current_unknown_index + 1) in not_gifted:
        # If the friend wants to give a gift to themselves, swap with next
        if i < len(unknown_indices) - 1:
            not_gifted[i], not_gifted[i + 1] = not_gifted[i + 1], not_gifted[i]
    
    f[current_unknown_index] = not_gifted[i]  # Update the gift list

print(" ".join(map(str, f)))