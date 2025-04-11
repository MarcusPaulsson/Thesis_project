n = int(input())
a = list(map(int, input().split()))

max_a = max(a)
min_a = min(a)

# Count occurrences of max and min
count_max = a.count(max_a)
count_min = a.count(min_a)

# Calculate possible instabilities
if count_max > 1:
    instability_remove_max = max_a - min_a
else:
    instability_remove_max = max(a[:-1]) - min(a[:-1])

if count_min > 1:
    instability_remove_min = max_a - min_a
else:
    instability_remove_min = max(a[1:]) - min(a[1:])

# The minimum instability after removing one element
result = min(instability_remove_max, instability_remove_min)
print(result)