n, m, d = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the minimum required space to place the platforms
min_required_space = sum(c) + (m - 1)

# If the minimum required space is greater than n, it's impossible
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
        # Move to the next position after the current platform
        position += 1  # Leave at least one cell gap

    print(" ".join(map(str, a)))