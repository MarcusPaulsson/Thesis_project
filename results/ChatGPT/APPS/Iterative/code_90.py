n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of platforms
total_length = sum(c)

# If the maximum jump distance is greater than or equal to the width of the river, it's always possible
if d >= n + 1:
    print("YES")
    print("0 " + "0 " * (n - 1) + str(m))
    exit()

# Check if we can place the platforms such that we can reach the end
# We need to ensure that the gaps between platforms do not exceed d
positions = []
current_position = 1

for length in c:
    positions.append(current_position)
    current_position += length

# Check if the gaps between the platforms can be filled with jumps
for i in range(1, len(positions)):
    gap = positions[i] - (positions[i - 1] + c[i - 1])
    if gap > d:
        print("NO")
        exit()

# Check the gap before the first platform and after the last platform
if positions[0] - 1 > d or (n + 1) - (positions[-1] + c[-1]) > d:
    print("NO")
    exit()

# If we can place the platforms, let's construct the output
result = [0] * n
current_position = 0

for i in range(m):
    for j in range(c[i]):
        result[current_position] = i + 1
        current_position += 1
    if i < m - 1:
        current_position += d - c[i]  # Leave a gap of at most d

print("YES")
print(" ".join(map(str, result)))