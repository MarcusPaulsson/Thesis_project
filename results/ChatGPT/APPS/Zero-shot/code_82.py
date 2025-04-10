n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0

# Solve from the left
while count < n and a[count] <= k:
    count += 1

# Solve from the right
while count < n and a[n - 1 - (count - (n - count))] <= k:
    count += 1

# Adjust for double counting if both ends are solvable
if count > n:
    count = n

print(count)