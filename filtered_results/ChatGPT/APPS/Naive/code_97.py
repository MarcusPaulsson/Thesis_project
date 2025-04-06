def min_coins_to_move_chips(n, positions):
    # Count the number of chips at even and odd positions
    even_count = sum(1 for x in positions if x % 2 == 0)
    odd_count = n - even_count
    
    # The minimum cost to move all chips to the same parity (either all even or all odd)
    return min(even_count, odd_count)

# Read input
n = int(input())
positions = list(map(int, input().split()))

# Get the result and print it
result = min_coins_to_move_chips(n, positions)
print(result)