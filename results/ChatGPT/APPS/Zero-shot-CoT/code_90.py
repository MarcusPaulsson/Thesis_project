def can_cross_river(n, m, d, c):
    total_platform_length = sum(c)
    # If the maximum jump distance is greater than or equal to the width of the river,
    # we can directly reach the other side.
    if d >= n + 1:
        print("YES")
        print("0 " * n + "1")  # All cells can be empty except the last one.
        return

    # We need to check if we can position the platforms such that we can jump across
    # the gaps between them. We will attempt to place them as left as possible.
    places = [0] * n
    current_position = 0

    for index in range(m):
        platform_length = c[index]
        if current_position + platform_length > n:
            print("NO")
            return
        # Place the platform
        for i in range(platform_length):
            places[current_position + i] = index + 1
        current_position += platform_length

        # Leave a gap of d between the platforms if possible
        if index < m - 1:  # No gap needed after the last platform
            current_position += d
    
    # Check if we can reach the end (n + 1) after placing all platforms
    if current_position > n:
        print("NO")
        return

    print("YES")
    print(" ".join(map(str, places)))

# Read input
n, m, d = map(int, input().split())
c = list(map(int, input().split()))
can_cross_river(n, m, d, c)