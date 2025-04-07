def min_instability(n, a):
    # Sort the array to easily find max and min after removing one element
    a.sort()
    
    # Calculate the two possible instabilities after removing one element
    instability1 = a[-1] - a[1]  # Remove the smallest element
    instability2 = a[-2] - a[0]  # Remove the largest element
    
    # Return the minimum of the two calculated instabilities
    return min(instability1, instability2)

# Read input
n = int(input())
a = list(map(int, input().split()))

# Get the result and print it
result = min_instability(n, a)
print(result)