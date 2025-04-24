def min_D_to_equalize(n, a):
    min_a = min(a)
    max_a = max(a)

    if max_a == min_a:
        return 0

    difference = max_a - min_a

    if difference % 2 == 0:
        return difference // 2
    return -1

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(min_D_to_equalize(n, a))