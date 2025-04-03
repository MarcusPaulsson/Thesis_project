import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve():
    n = int(input())
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.append(n)
    divisors.sort()

    import itertools
    
    best_order = None
    min_moves = float('inf')

    for order in itertools.permutations(divisors):
        moves = 0
        
        current_list = list(order)
        
        is_decrypted = False
        
        while not is_decrypted:
            is_decrypted = True
            new_list = []
            for i in range(len(current_list)):
                new_list.append(current_list[i])
                
                
                if gcd(current_list[i], current_list[(i+1) % len(current_list)]) == 1:
                    is_decrypted = False
                    lcm = (current_list[i] * current_list[(i+1) % len(current_list)]) // gcd(current_list[i], current_list[(i+1) % len(current_list)])
                    new_list.append(lcm)
                    moves += 1
            current_list = new_list
        
        if moves < min_moves:
            min_moves = moves
            best_order = order

    print(*best_order)
    print(min_moves)

t = int(input())
for _ in range(t):
    solve()