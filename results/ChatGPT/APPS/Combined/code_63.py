def minimum_instability(n, a):
    if n <= 2:
        return 0  # If there are only two elements, removing one will always result in zero instability

    a.sort()
    # Calculate the instability after removing the smallest or the largest element
    instability_remove_min = a[-1] - a[1]  # Remove the smallest element
    instability_remove_max = a[-2] - a[0]  # Remove the largest element
    
    return min(instability_remove_min, instability_remove_max)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(minimum_instability(n, a))