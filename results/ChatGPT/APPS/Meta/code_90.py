def can_reach(n, m, d, c):
    # Initialize the result array with zeros
    result = [0] * n
    
    # Position to place the platforms
    current_position = 1  # starts from 1 since 0 is the left bank

    # Place each platform
    for i in range(m):
        platform_length = c[i]
        
        # Place the platform at the current position
        for j in range(platform_length):
            result[current_position - 1 + j] = i + 1  # 1-indexed platform
        current_position += platform_length

        # If we can place the next platform, we need to ensure there's space.
        if i < m - 1:  # If there is another platform
            current_position += 1  # Leave a gap for jumping

    # Now we need to check if we can reach n + 1 from 0
    # We can reach n + 1 if the last platform can be accessed
    if current_position - 1 <= n:
        print("YES")
        print(" ".join(map(str, result)))
    else:
        print("NO")

# Input reading
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

can_reach(n, m, d, c)