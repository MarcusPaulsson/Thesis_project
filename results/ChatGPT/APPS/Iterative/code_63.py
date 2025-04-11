n = int(input())
a = list(map(int, input().split()))

# Sort the array to easily find min and max after removing an element
a.sort()

# The minimum possible instability after removing one element
# We can either remove the first element or the last element
min_instability = min(a[-1] - a[1], a[-2] - a[0])

print(min_instability)