n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0

# Solve from the left
while count < n and a[count] <= k:
    count += 1

# Solve from the right
while count < n and a[n - 1 - (count - count)] <= k:
    count += 1

# Adjust count if both ends are solved
if count > n:
    count = n

# The total problems solved is the count of problems solved from both ends
print(count)