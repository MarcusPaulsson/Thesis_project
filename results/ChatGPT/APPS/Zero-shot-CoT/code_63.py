def minimum_instability(n, a):
    a.sort()
    
    # To minimize instability after removing one element, we can either:
    # 1. Remove the maximum element (last element in sorted array)
    # 2. Remove the minimum element (first element in sorted array)
    
    # If we remove the maximum element
    instability_remove_max = a[-2] - a[0]
    
    # If we remove the minimum element
    instability_remove_min = a[-1] - a[1]
    
    # The minimum instability after removing one element
    return min(instability_remove_max, instability_remove_min)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Get the result and print it
result = minimum_instability(n, a)
print(result)