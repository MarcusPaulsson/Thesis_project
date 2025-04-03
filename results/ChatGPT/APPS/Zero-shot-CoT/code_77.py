def min_difference(n):
    total_sum = n * (n + 1) // 2
    return total_sum % 2

n = int(input())
print(min_difference(n))