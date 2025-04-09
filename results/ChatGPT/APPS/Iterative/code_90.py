n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the minimum required position to reach the last cell (n + 1)
required_length = sum(c) + (m - 1)  # platforms + gaps

if required_length > n:
    print("NO")
else:
    print("YES")
    a = [0] * n
    current_position = 0
    
    for i in range(m):
        # Place the platform
        for j in range(c[i]):
            a[current_position] = i + 1  # platform index is 1-based
            current_position += 1
        # Add gap only if this is not the last platform
        if i < m - 1:
            current_position += 1  # gap between platforms

    print(" ".join(map(str, a)))