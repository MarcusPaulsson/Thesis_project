def game_23(n, m):
    if m % n != 0:
        return -1
    
    ratio = m // n
    count_2 = 0
    count_3 = 0
    
    while ratio % 2 == 0:
        ratio //= 2
        count_2 += 1
        
    while ratio % 3 == 0:
        ratio //= 3
        count_3 += 1
    
    if ratio != 1:
        return -1
    
    return count_2 + count_3

# Read input
n, m = map(int, input().split())
# Get the result and print it
print(game_23(n, m))