n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0

# Solve from the left
while count < n and a[count] <= k:
    count += 1

# Solve from the right
right_count = 0
while right_count < n and a[n - 1 - right_count] <= k:
    right_count += 1

# Adjust count to avoid double counting if both ends are solved
if count + right_count > n:
    count = n
else:
    count += right_count

print(count)