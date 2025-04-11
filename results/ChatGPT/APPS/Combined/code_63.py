def minimum_instability(n, a):
    # Sort the array to easily find min and max after removing one element
    a.sort()
    
    # Calculate the instability after removing the first or the last element
    instability_remove_first = a[-1] - a[1]  # Remove the smallest element
    instability_remove_last = a[-2] - a[0]   # Remove the largest element
    
    # The minimum instability after removing one element
    return min(instability_remove_first, instability_remove_last)

# Input reading
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output the result
print(minimum_instability(n, a))