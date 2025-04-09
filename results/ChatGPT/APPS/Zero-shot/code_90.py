n, m, d = map(int, input().split())
c = list(map(int, input().split()))

total_length = sum(c)

# Check if we can fit the platforms in such a way that we can reach n+1
if total_length + (m - 1) * d < n:
    print("NO")
else:
    print("YES")
    a = [0] * n
    pos = 0

    for i in range(m):
        # Place the platform at the current position
        for j in range(c[i]):
            a[pos] = i + 1
            pos += 1
        # Move to the next position considering the jump distance
        if i < m - 1:
            pos += d  # leave space for the next platform

    print(" ".join(map(str, a)))