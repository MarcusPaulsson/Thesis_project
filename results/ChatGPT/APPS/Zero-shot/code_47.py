def min_coins_to_move_chips(n, x):
    even_count = sum(1 for pos in x if pos % 2 == 0)
    odd_count = n - even_count
    return min(even_count, odd_count)

n = int(input())
x = list(map(int, input().split()))
print(min_coins_to_move_chips(n, x))