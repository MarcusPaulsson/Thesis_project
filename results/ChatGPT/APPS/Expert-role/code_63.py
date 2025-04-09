def min_instability(n, a):
    a.sort()
    
    # Remove the first element or the last element
    instability_remove_first = a[-1] - a[1]
    instability_remove_last = a[-2] - a[0]
    
    return min(instability_remove_first, instability_remove_last)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_instability(n, a))