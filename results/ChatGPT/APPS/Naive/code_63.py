def min_instability(n, a):
    a.sort()
    # The minimum instability can be achieved by removing either the first or the last element
    instability_remove_min = a[-1] - a[1]  # Remove the minimum element
    instability_remove_max = a[-2] - a[0]  # Remove the maximum element
    return min(instability_remove_min, instability_remove_max)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_instability(n, a))