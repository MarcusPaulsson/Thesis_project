def min_coins_to_move_chips(n, chips):
    even_count = sum(1 for x in chips if x % 2 == 0)
    odd_count = n - even_count
    return min(even_count, odd_count)

# Input reading
n = int(input())
chips = list(map(int, input().split()))

# Calculate and print the result
print(min_coins_to_move_chips(n, chips))