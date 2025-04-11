n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the minimum required space to place the platforms
total_length = sum(c)
min_required_space = total_length + (m - 1)  # total length + gaps between platforms

if min_required_space > n:
    print("NO")
else:
    print("YES")
    a = [0] * n
    position = 0

    for i in range(m):
        for j in range(c[i]):
            a[position] = i + 1
            position += 1
        if i < m - 1:  # Add a gap of at least 1 cell between platforms
            position += 1

    print(" ".join(map(str, a)))