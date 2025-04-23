def can_reach_end(n, m, d, c):
    total_length = sum(c)

    # If the maximum jump distance is greater than or equal to the width of the river
    if d >= n + 1:
        print("YES")
        print("0 " + "0 " * (n - 1) + str(m))
        return

    # Calculate the minimum required gap between platforms
    min_required_gap = (m - 1) * d

    # If the total length of platforms plus the minimum required gaps exceeds n, it's impossible
    if total_length + min_required_gap > n:
        print("NO")
        return

    # Initialize the result array with zeros
    result = [0] * n
    position = 0

    for i in range(m):
        # Place the platform at the current position
        for j in range(c[i]):
            result[position] = i + 1
            position += 1
        # Move the position to the right by d for the next platform
        position += d

    print("YES")
    print(" ".join(map(str, result)))

# Read input
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Call the function
can_reach_end(n, m, d, c)