def min_coins_to_move_chips(n, positions):
    even_count = sum(1 for x in positions if x % 2 == 0)
    odd_count = n - even_count
    return min(even_count, odd_count)

if __name__ == "__main__":
    n = int(input().strip())
    positions = list(map(int, input().strip().split()))
    print(min_coins_to_move_chips(n, positions))