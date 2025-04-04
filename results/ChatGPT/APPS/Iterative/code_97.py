n = int(input())
x = list(map(int, input().split()))

even_count = sum(1 for i in x if i % 2 == 0)
odd_count = n - even_count

print(min(even_count, odd_count))