def minimum_instability(n, a):
    # Sort the array to easily find min and max after removing an element
    a.sort()
    
    # Calculate potential minimum instability after removing one element
    instability_case1 = a[-1] - a[1]  # Remove the first element
    instability_case2 = a[-2] - a[0]  # Remove the last element
    
    # The minimum instability after removing one element
    return min(instability_case1, instability_case2)

# Input reading
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output the result
print(minimum_instability(n, a))