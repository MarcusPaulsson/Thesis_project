def min_instability(n, a):
    # Sort the array to easily find the max and min after removing one element
    a.sort()

    # The instability after removing the first or last element
    instability_remove_first = a[-1] - a[1]
    instability_remove_last = a[-2] - a[0]

    # The minimum instability will be the minimum of the two calculated values
    return min(instability_remove_first, instability_remove_last)

# Read input
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the minimum possible instability
print(min_instability(n, a))