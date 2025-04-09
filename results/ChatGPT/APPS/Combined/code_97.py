def min_coins_to_move_chips(n, positions):
    odd_count = sum(1 for pos in positions if pos % 2 != 0)
    even_count = n - odd_count
    return min(odd_count, even_count)

# Read input
n = int(input().strip())
positions = list(map(int, input().strip().split()))

# Calculate and print the result
result = min_coins_to_move_chips(n, positions)
print(result)