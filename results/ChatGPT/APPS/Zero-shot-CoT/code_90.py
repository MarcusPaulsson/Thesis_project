n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of platforms
total_length = sum(c)

# If the maximum jump distance is greater than or equal to the width of the river,
# we can always reach the other side.
if d >= n + 1:
    print("YES")
    print("0 " + "0 " * (n - total_length) + " ".join(str(i + 1) for i in range(m)))
else:
    # We need to check if we can place the platforms such that we can jump across
    # We will try to place the platforms with at least `d` distance between them
    positions = []
    current_position = 0

    for i in range(m):
        positions.append(current_position)
        current_position += c[i]

        # Ensure there's enough space for the next platform
        if i < m - 1:
            current_position += d

    # Check if the last platform can reach the end
    if positions[-1] + c[-1] + d < n + 1:
        print("NO")
    else:
        print("YES")
        result = [0] * n
        for i in range(m):
            for j in range(c[i]):
                result[positions[i] + j] = i + 1
        print(" ".join(map(str, result)))