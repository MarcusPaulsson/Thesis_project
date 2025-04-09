def min_coins_to_move_chips(n, chips):
    odd_count = sum(1 for x in chips if x % 2 == 1)
    even_count = n - odd_count
    return min(odd_count, even_count)

n = int(input())
chips = list(map(int, input().split()))
print(min_coins_to_move_chips(n, chips))