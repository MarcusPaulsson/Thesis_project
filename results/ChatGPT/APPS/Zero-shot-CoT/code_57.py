n = int(input())
f = list(map(int, input().split()))

# Track the friends who have not been assigned a gift
gifted = set(f) - {0}
unknown = [i for i in range(1, n + 1) if i not in gifted]
to_assign = [i for i in range(n) if f[i] == 0]

# Assign the gifts for those who have '0'
for i in range(len(to_assign)):
    friend_index = to_assign[i]
    # Choose a gift recipient from unknown
    recipient = unknown[i]
    # Ensure that the assignment is valid (no self-gifting)
    if recipient == friend_index + 1:  # +1 because friend_index is 0-based
        # If it is, swap with the next one (wrap around if necessary)
        recipient = unknown[(i + 1) % len(unknown)]
    
    f[friend_index] = recipient

print(" ".join(map(str, f)))