n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length of platforms
total_length = sum(c)

# Check if we can place the platforms with the given jump distance
if total_length + (m - 1) * d < n:
    print("NO")
else:
    print("YES")
    a = [0] * n
    current_position = 0
    
    for i in range(m):
        # Place the platform at the current position
        for j in range(c[i]):
            a[current_position + j] = i + 1
        current_position += c[i]
        
        # Move to the next position considering the jump distance
        if i < m - 1:
            current_position += d
    
    print(" ".join(map(str, a)))