n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of platforms
total_length = sum(c)

# If the maximum jump distance is greater than or equal to n, we can always reach the end
if d >= n:
    print("YES")
    print("0 " * n + str(1))
    exit()

# Check if we can fit the platforms within the constraints
# We need to ensure that the gaps between platforms allow for jumping
# The maximum gap we can have between platforms is d
# We will place the platforms starting from position 1

positions = []
current_position = 1

for i in range(m):
    positions.append((current_position, current_position + c[i] - 1))
    current_position += c[i]

# Now we need to check if we can place the platforms with the required gaps
# The last platform must end at or before n
if positions[-1][1] > n:
    print("NO")
    exit()

# We can place the platforms, now we need to fill the output array
a = [0] * n

# Fill the array with platform indices
for index, (start, end) in enumerate(positions):
    for i in range(start - 1, end):
        a[i] = index + 1

# Check if we can jump from the last platform to n + 1
if positions[-1][1] + d < n + 1:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, a)))