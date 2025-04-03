n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Initialize the river cells with zeros
a = [0] * n

# Calculate the total length of platforms
total_length = sum(c)

# Check if we can reach n + 1
if total_length + (m - 1) * d < n:
    print("NO")
else:
    print("YES")
    
    # Place platforms in the array
    position = 0
    for i in range(m):
        # Set the platform index in the cells
        for j in range(c[i]):
            a[position] = i + 1
            position += 1
        # Move the position by d after each platform, if not the last platform
        if i < m - 1:
            position += d
            
    print(' '.join(map(str, a)))