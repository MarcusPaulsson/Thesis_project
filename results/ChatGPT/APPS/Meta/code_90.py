n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of platforms
total_length = sum(c)

# If the maximum jump distance is greater than or equal to the width of the river, we can always reach the other side
if d >= n + 1:
    print("YES")
    print("0 " + " ".join(str(1) for _ in range(c[0])) + " " + "0 " * (n - total_length) + " " + " ".join(str(i + 2) for i in range(1, m)))
    exit()

# Check if we can fit the platforms within the jump distance constraints
positions = []
current_position = 1  # Start placing platforms from position 1

for i in range(m):
    positions.append(current_position)
    current_position += c[i]

# Check if the last platform can be reached from the last position
if positions[-1] - 1 > d:
    print("NO")
else:
    print("YES")
    result = [0] * n
    current_position = 0
    for i in range(m):
        for j in range(c[i]):
            result[current_position] = i + 1
            current_position += 1
        if i < m - 1:
            current_position += 1  # Leave a gap of at least 1 cell between platforms
    print(" ".join(map(str, result)))