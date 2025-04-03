def min_instability(n, a):
    a.sort()
    # Removing the smallest element or the largest element
    instability1 = a[-1] - a[1]  # removing the first element
    instability2 = a[-2] - a[0]  # removing the last element
    return min(instability1, instability2)

n = int(input())
a = list(map(int, input().split()))
print(min_instability(n, a))