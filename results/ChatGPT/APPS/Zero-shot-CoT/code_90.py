n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the maximum distance we need to cover
max_distance = n + 1

# Calculate the total length of platforms
total_length = sum(c)

if total_length > n:
    print("NO")
    exit()

# Initialize the river cells
a = [0] * n

# We will place platforms in a way that maximizes the distance between them
position = 0
for i in range(m):
    # Place platform i at the current position
    for j in range(c[i]):
        a[position] = i + 1
        position += 1
    # Move position to the right to ensure platforms do not intersect
    if i < m - 1:
        position += d - c[i]  # Leave a gap of d between platforms

# Check if we can reach n + 1
if position > n:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, a)))