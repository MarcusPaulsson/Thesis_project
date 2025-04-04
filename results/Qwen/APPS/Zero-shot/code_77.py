def min_diff(n):
    total_sum = n * (n + 1) // 2
    if total_sum % 2 == 0:
        return 0
    else:
        return 1

n = int(input())
print(min_diff(n))