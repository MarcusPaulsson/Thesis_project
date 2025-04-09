n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0

# Solve from the left
while count < n and a[count] <= k:
    count += 1

# Solve from the right
while count < n and a[n - 1 - (count - count)] <= k:
    count += 1

# Subtract the number of problems that were counted twice
count = min(count, n)

print(count)