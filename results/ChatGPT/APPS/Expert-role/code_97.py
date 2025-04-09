n = int(input())
positions = list(map(int, input().split()))

even_count = sum(1 for x in positions if x % 2 == 0)
odd_count = n - even_count

# The minimum number of coins needed is the smaller of the two counts
result = min(even_count, odd_count)
print(result)