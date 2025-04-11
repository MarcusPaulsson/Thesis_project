n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of platforms
total_length = sum(c)

# If the maximum jump distance is greater than or equal to n, we can always reach the end
if d >= n:
    print("YES")
    print("0 " * n + str(m))
    exit()

# We need to check if we can place the platforms such that we can jump from 0 to n + 1
# The maximum distance we can jump is d, so we need to ensure that the gaps between platforms
# do not exceed d.

# Start placing platforms
a = [0] * n
current_position = 0

# Place platforms in the array
for i in range(m):
    for j in range(c[i]):
        a[current_position + j] = i + 1
    current_position += c[i]

# Check if we can jump from the end of the last platform to n + 1
if current_position + d >= n + 1:
    print("YES")
    print(" ".join(map(str, a)))
else:
    # Check for gaps between platforms
    gap = d
    last_position = 0
    
    for i in range(m):
        # Check if we can jump from the last position to the start of the current platform
        if last_position + gap < current_position:
            print("NO")
            exit()
        last_position += c[i]

    # Final check from the last platform to n + 1
    if last_position + d >= n + 1:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")