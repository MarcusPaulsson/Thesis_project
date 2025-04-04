def minimum_instability(n, a):
    a.sort()
    # Remove first or last element to minimize instability
    instability1 = a[-1] - a[1]  # Remove the first element
    instability2 = a[-2] - a[0]  # Remove the last element
    return min(instability1, instability2)

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
print(minimum_instability(n, a))