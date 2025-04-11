n = int(input())
chips = list(map(int, input().split()))

even_count = sum(1 for x in chips if x % 2 == 0)
odd_count = n - even_count

# Minimum coins required to move all chips to the same coordinate
result = min(even_count, odd_count)
print(result)