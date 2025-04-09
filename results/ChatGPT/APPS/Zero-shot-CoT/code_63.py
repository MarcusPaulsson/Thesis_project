n = int(input())
a = list(map(int, input().split()))

# Sort the array to easily find max and min after removing one element.
a.sort()

# The minimum instability after removing one element can be achieved by:
# 1. Removing the first element (minimum value) and checking the range of the rest.
# 2. Removing the last element (maximum value) and checking the range of the rest.
min_instability = min(a[-1] - a[1], a[-2] - a[0])

print(min_instability)