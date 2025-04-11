def min_instability(n, a):
    a.sort()
    # The minimum instability after removing one element can be found by considering
    # removing the smallest or the largest element.
    instability1 = a[-1] - a[1]  # Remove the smallest element
    instability2 = a[-2] - a[0]  # Remove the largest element
    return min(instability1, instability2)

n = int(input())
a = list(map(int, input().split()))
print(min_instability(n, a))