def min_instability(n, a):
    a.sort()
    # Remove the smallest element or the largest element
    instability_remove_min = a[-1] - a[1]  # Remove the smallest element
    instability_remove_max = a[-2] - a[0]  # Remove the largest element
    return min(instability_remove_min, instability_remove_max)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_instability(n, a))