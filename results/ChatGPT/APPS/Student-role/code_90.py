n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the total length required for the platforms including gaps
total_length = sum(c) + (m - 1)

# Maximum reach from the first position (0)
max_reach = d * (total_length // d)

if total_length > n or max_reach < n:
    print("NO")
else:
    print("YES")
    a = [0] * n
    position = 0

    for i in range(m):
        for j in range(c[i]):
            if position < n:
                a[position] = i + 1
                position += 1
        if i < m - 1:
            position += 1  # Leave a gap of at least 1 cell between platforms

    print(" ".join(map(str, a)))