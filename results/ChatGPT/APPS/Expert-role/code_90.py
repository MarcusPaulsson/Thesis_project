def can_reach_end(n, m, d, c):
    # Calculate the total length of platforms
    total_length = sum(c)
    
    # If the maximum jump distance is greater than or equal to n, we can always reach the end
    if d >= n + 1:
        print("YES")
        print("0 " * n + str(1))
        return
    
    # Initialize the river representation
    river = [0] * n
    
    # Start placing platforms
    current_position = 0
    for i in range(m):
        # Place the platform at the current position
        for j in range(c[i]):
            if current_position < n:
                river[current_position] = i + 1
                current_position += 1
            else:
                break
    
    # Check if we can reach the end
    last_position = -1
    for i in range(n):
        if river[i] != 0:
            last_position = i
    
    # Check if we can jump from the last platform to the end
    if last_position == -1 or (last_position + d < n + 1):
        print("NO")
        return
    
    # Output the result
    print("YES")
    print(" ".join(map(str, river)))

# Read input
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

can_reach_end(n, m, d, c)