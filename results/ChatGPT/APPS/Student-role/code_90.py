n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the minimum space needed to place the platforms
min_space_needed = sum(c) + (m - 1)  # Total length of platforms + gaps between them

# Check if we can fit the platforms within the river width
if min_space_needed > n:
    print("NO")
else:
    print("YES")
    a = [0] * n
    pos = 0
    
    # Place each platform in the array
    for i in range(m):
        for j in range(c[i]):
            a[pos] = i + 1  # Platform indices are 1-based
            pos += 1
        if i < m - 1:  # If not the last platform, leave a gap
            pos += 1  # Move one cell to create a gap

    print(" ".join(map(str, a)))