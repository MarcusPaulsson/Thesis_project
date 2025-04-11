def min_instability(n, a):
    a.sort()
    # The minimum instability can be achieved by removing either the first or the last element
    return min(a[-1] - a[1], a[-2] - a[0])

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_instability(n, a))