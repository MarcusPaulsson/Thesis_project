n = int(input())
a = list(map(int, input().split()))

# Sort the array to easily find min and max after removing elements
a.sort()

# Two potential scenarios:
# 1. Remove the first element (smallest)
# 2. Remove the last element (largest)

# Instability after removing the first element
instability1 = a[-1] - a[1]

# Instability after removing the last element
instability2 = a[-2] - a[0]

# The minimum instability after removing one element
min_instability = min(instability1, instability2)

print(min_instability)