def min_instability(n, a):
    a.sort()
    # Calculate instability after removing the first or the last element
    return min(a[-1] - a[1], a[-2] - a[0])

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Get the result and print it
result = min_instability(n, a)
print(result)