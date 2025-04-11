def minimum_instability(n, a):
    # Sort the array to easily find the min and max after removing an element
    a.sort()
    
    # Calculate the minimum instability after removing one element
    instability_remove_min = a[-1] - a[1]  # Remove the smallest element
    instability_remove_max = a[-2] - a[0]  # Remove the largest element
    
    # Return the minimum instability
    return min(instability_remove_min, instability_remove_max)

# Example usage:
# n = int(input())
# a = list(map(int, input().split()))
# print(minimum_instability(n, a))