n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0

# Solve from the left
while count < n and a[count] <= k:
    count += 1

# Solve from the right
while count < n and a[n - 1 - (count - count)] <= k:
    count += 1

# The count could have counted the overlap in the middle
# So we need to ensure we don't double count the last problem
if count > n:
    count = n

print(count)