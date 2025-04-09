n = int(input())
chips = list(map(int, input().split()))

# Count the number of chips on even and odd positions
even_count = sum(1 for x in chips if x % 2 == 0)
odd_count = n - even_count  # Since total chips are n

# The minimum coins required is the smaller of the two counts
min_coins = min(even_count, odd_count)

print(min_coins)