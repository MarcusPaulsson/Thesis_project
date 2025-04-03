n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of platforms
total_length = sum(c)

# If the maximum jump distance is greater than or equal to the width of the river plus one,
# we can always reach the other side
if d >= n + 1:
    print("YES")
    print("0 " * n + "1")
else:
    # Try to place the platforms
    a = [0] * n
    position = 0

    for i in range(m):
        if position + c[i] > n:
            print("NO")
            exit()
        
        # If we can place the platform at the current position
        for j in range(c[i]):
            a[position + j] = i + 1  # Fill with platform index
        position += c[i]

        # Leave space for the next platform
        if i < m - 1:  # Don't skip space after the last platform
            position += 1

    # Check if we can reach the last position from the last platform
    if position - 1 + d < n:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, a)))