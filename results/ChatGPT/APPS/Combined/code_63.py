def minimum_instability(n, a):
    # Sort the array to easily access the minimum and maximum values
    a.sort()
    
    # Calculate the instability for the two cases of removal
    instability_remove_min = a[-1] - a[1]  # Remove minimum element
    instability_remove_max = a[-2] - a[0]  # Remove maximum element
    
    # Return the minimum instability after removing one element
    return min(instability_remove_min, instability_remove_max)

# Input reading
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output the result
print(minimum_instability(n, a))