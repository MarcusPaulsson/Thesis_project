def can_cross_river(n, m, d, c):
    # Calculate the total length of platforms
    total_length = sum(c)
    
    # If the maximum jump distance is greater than or equal to the river width
    if d >= n + 1:
        print("YES")
        print("0 " + "0 " * (n - 1) + str(m))
        return
    
    # Initialize the river representation
    river = [0] * n
    current_position = 0
    
    # Place platforms in the river
    for i in range(m):
        # Check if we can place the platform
        if current_position + c[i] > n:
            print("NO")
            return
        
        # Place the platform
        for j in range(c[i]):
            river[current_position + j] = i + 1
        
        # Move the current position to the end of the current platform
        current_position += c[i]
        
        # Ensure there is enough space for the next jump
        if i < m - 1:
            current_position += 1  # Leave at least one cell gap between platforms
    
    # Check if we can reach the end
    last_platform_end = current_position - 1
    if last_platform_end + d >= n:
        print("YES")
        print(" ".join(map(str, river)))
    else:
        print("NO")

# Read input
n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Call the function
can_cross_river(n, m, d, c)