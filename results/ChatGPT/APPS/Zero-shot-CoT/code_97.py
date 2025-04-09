n = int(input())
chips = list(map(int, input().split()))

even_count = sum(1 for x in chips if x % 2 == 0)
odd_count = n - even_count

# The minimum coins required will be the smaller of the two groups (even or odd)
min_coins = min(even_count, odd_count)

print(min_coins)