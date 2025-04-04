def min_instability(n, a):
    # Sort the array to easily find the min and max values after removing an element
    a.sort()
    
    # The instability after removing the first or the last element
    instability_remove_first = a[-1] - a[1]  # Remove the first element
    instability_remove_last = a[-2] - a[0]   # Remove the last element
    
    # The minimum instability
    return min(instability_remove_first, instability_remove_last)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_instability(n, a))