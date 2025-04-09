n = int(input())
a = list(map(int, input().split()))

# Sort the array to easily find min and max after removing an element
a.sort()

# The minimum instability after removing one element can be found by considering
# removing either the smallest element or the largest element.
# The candidates for instability are:
# 1. Remove the largest element: instability = a[n-2] - a[0]
# 2. Remove the smallest element: instability = a[n-1] - a[1]

min_instability = min(a[n-2] - a[0], a[n-1] - a[1])

print(min_instability)