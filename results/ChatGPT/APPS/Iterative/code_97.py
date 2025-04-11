n = int(input())
chips = list(map(int, input().split()))

even_count = sum(1 for x in chips if x % 2 == 0)
odd_count = n - even_count

# The minimum cost is the number of chips that are in the minority
print(min(even_count, odd_count))