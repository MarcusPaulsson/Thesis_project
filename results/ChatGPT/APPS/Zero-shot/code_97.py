n = int(input())
x = list(map(int, input().split()))

even_count = sum(1 for i in x if i % 2 == 0)
odd_count = n - even_count

# Minimum coins needed to move all chips to the same coordinate
result = min(even_count, odd_count)
print(result)