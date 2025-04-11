n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of platforms
total_length = sum(c)

# If the maximum jump distance is greater than or equal to the width of the river, we can always reach the end
if d >= n + 1:
    print("YES")
    print("0 " + "0 " * (n - 1) + "1")
else:
    # We need to check if we can place the platforms in a way that allows us to jump across
    # We will try to place the platforms starting from the leftmost position
    a = [0] * n
    current_position = 0
    
    for i in range(m):
        # Place the platform at the current position
        for j in range(c[i]):
            if current_position < n:
                a[current_position] = i + 1
                current_position += 1
        
        # Move to the next position after the platform
        current_position += 1  # Leave at least one cell gap after each platform
    
    # Check if we can reach the end
    reachable = True
    last_position = -1
    
    for i in range(n):
        if a[i] != 0:
            last_position = i
        if last_position != -1 and i - last_position > d:
            reachable = False
            break
    
    if reachable:
        print("YES")
        print(" ".join(map(str, a)))
    else:
        print("NO")