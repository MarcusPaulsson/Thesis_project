n = int(input())
a = list(map(int, input().split()))

# Sort the array to easily find min and max after removing one element
a.sort()

# The minimum instability after removing one element can be found by considering
# two cases: removing the smallest element or removing the largest element.
# After removing the smallest element, the new min is a[1] and max is a[n-1].
# After removing the largest element, the new min is a[0] and max is a[n-2].

# Calculate the two possible instabilities
instability_remove_min = a[-1] - a[1]
instability_remove_max = a[-2] - a[0]

# The minimum instability after removing one element
min_instability = min(instability_remove_min, instability_remove_max)

print(min_instability)