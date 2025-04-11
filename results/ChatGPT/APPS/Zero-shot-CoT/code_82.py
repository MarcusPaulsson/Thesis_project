n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0

# Solve from the left
while count < n and a[count] <= k:
    count += 1

# Solve from the right
while count < n and a[n - 1 - (count - (n - len(a)))] <= k:
    count += 1

# Adjust count if we counted the same problem from both ends
if count > n:
    count = n

print(count)