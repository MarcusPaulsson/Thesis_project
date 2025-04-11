n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the minimum required length to place all platforms
total_length = sum(c)
if total_length + (m - 1) > n:
    print("NO")
    exit()

# Create the result array
result = [0] * n
current_position = 0

# Place the platforms
for i in range(m):
    # Place platform i (1-indexed)
    for j in range(c[i]):
        result[current_position] = i + 1
        current_position += 1
    # Move to the next position after the platform
    if i < m - 1:
        current_position += 1  # Leave at least one cell gap

print("YES")
print(" ".join(map(str, result)))