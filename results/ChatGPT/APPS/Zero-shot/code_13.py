def min_instability(n, a):
    if n == 2:
        return 0  # If only 2 elements, removing one will always lead to 0 instability

    a.sort()  # Sort the array to easily find max and min after removal

    # Remove the first element (minimum) or the last element (maximum)
    instability_remove_min = a[-1] - a[1]  # Remove the smallest element
    instability_remove_max = a[-2] - a[0]  # Remove the largest element

    # Return the minimum of the two calculated instabilities
    return min(instability_remove_min, instability_remove_max)

# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_instability(n, a))