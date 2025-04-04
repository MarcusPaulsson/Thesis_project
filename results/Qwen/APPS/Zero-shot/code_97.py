def min_coins_to_move_chips(n, chips):
    odd_count = sum(1 for chip in chips if chip % 2 != 0)
    even_count = n - odd_count
    return min(odd_count, even_count)

n = int(input())
chips = list(map(int, input().split()))
print(min_coins_to_move_chips(n, chips))