def min_coins_to_move_chips(n, positions):
    even_count = sum(1 for pos in positions if pos % 2 == 0)
    odd_count = n - even_count
    return min(even_count, odd_count)

# Input reading
n = int(input().strip())
positions = list(map(int, input().strip().split()))

# Output the result
print(min_coins_to_move_chips(n, positions))