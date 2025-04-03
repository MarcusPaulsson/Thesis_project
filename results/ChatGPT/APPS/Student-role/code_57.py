n = int(input())
f = list(map(int, input().split()))

# Initialize lists to track givers and receivers
givers = []
receivers = set(range(1, n + 1))

# Fill known values and track the givers
for i in range(n):
    if f[i] != 0:
        givers.append((i + 1, f[i]))  # (friend_index, gives_to)
        receivers.discard(f[i])  # Remove from receivers

# Convert receivers to a list for filling unknowns
receivers = list(receivers)
k = len(givers)

# Now we fill the unknowns
for i in range(n):
    if f[i] == 0:
        # The current friend must give a gift to someone in receivers
        # We need to ensure they don't give to themselves
        f[i] = receivers.pop()  # Assign a receiver to the friend

# Now we need to ensure every friend receives exactly one gift
# Create a reverse mapping to keep track of who is receiving from whom
receive_map = [0] * (n + 1)
for i in range(n):
    if f[i] != 0:
        receive_map[f[i]] = i + 1

# Ensure that each friend gives a gift and receives one gift
for i in range(n):
    if f[i] == 0:
        # Find a valid receiver who is not the friend themselves
        for r in range(1, n + 1):
            if r != i + 1 and receive_map[r] == 0:
                f[i] = r
                receive_map[r] = i + 1
                break

print(" ".join(map(str, f)))