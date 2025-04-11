def min_coins_to_move_chips(n, positions):
    odd_count = sum(1 for x in positions if x % 2 != 0)
    even_count = n - odd_count
    return min(odd_count, even_count)

# Input reading
n = int(input())
positions = list(map(int, input().split()))

# Output the result
print(min_coins_to_move_chips(n, positions))