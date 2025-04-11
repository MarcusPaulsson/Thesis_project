def min_instability(n, a):
    # Sort the array to easily find the min and max after removing an element
    a.sort()
    
    # The minimum instability after removing one element can be calculated
    # by considering removing the smallest or the largest element
    # The two cases are:
    # 1. Remove the smallest element (a[0])
    # 2. Remove the largest element (a[n-1])
    
    instability_case1 = a[-1] - a[1]  # Remove the smallest element
    instability_case2 = a[-2] - a[0]  # Remove the largest element
    
    # The minimum instability is the minimum of the two cases
    return min(instability_case1, instability_case2)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_instability(n, a))