n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0

# Check from the left
while count < n and a[count] <= k:
    count += 1

# Check from the right
while count < n and a[n - 1 - (count - 1)] <= k:
    count += 1

# If we counted the same problem from both ends, subtract 1
if count > n:
    count = n

print(count)