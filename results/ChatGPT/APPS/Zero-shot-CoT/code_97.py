n = int(input())
x = list(map(int, input().split()))

even_count = sum(1 for xi in x if xi % 2 == 0)
odd_count = n - even_count

# The minimum coins required is the minimum of moving all to even or all to odd
print(min(even_count, odd_count))