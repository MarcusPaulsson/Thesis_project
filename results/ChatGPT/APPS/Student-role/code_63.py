n = int(input())
a = list(map(int, input().split()))

# Sort the array to easily find min and max
a.sort()

# Minimum possible instability after removing one element
# We can either remove the first element or the last element
# The resulting instability will be max - min of the remaining elements
min_instability = min(a[-1] - a[1], a[-2] - a[0])

print(min_instability)