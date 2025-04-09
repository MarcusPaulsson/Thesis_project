n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of all platforms
total_length = sum(c)

# If the max jump distance d is greater than or equal to n, we can always reach the end
if d >= n:
    result = [0] * n
    position = 0
    for i in range(m):
        for j in range(c[i]):
            result[position] = i + 1
            position += 1
    print("YES")
    print(" ".join(map(str, result)))
else:
    # Try to place the platforms
    result = [0] * n
    position = 0
    
    for i in range(m):
        # If the current platform can fit within the jump distance
        if position + c[i] - 1 <= n and (i == 0 or position - (c[i-1] if i > 0 else 0) <= d):
            for j in range(c[i]):
                result[position] = i + 1
                position += 1
        else:
            print("NO")
            exit(0)
        
        # Move the position to the next platform start
        if i < m - 1:
            position += d - c[i]
            position = max(position, sum(c[:i+1])) # Ensure we don't overlap
    
    print("YES")
    print(" ".join(map(str, result)))