def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve():
    n = int(input())
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.append(n)
    divisors.sort()

    import itertools
    
    best_order = None
    min_moves = float('inf')

    for order in itertools.permutations(divisors):
        moves = 0
        is_valid = True
        for i in range(len(order)):
            if gcd(order[i], order[(i+1) % len(order)]) == 1:
                is_valid = False
                break
        
        if is_valid:
            if moves < min_moves:
                min_moves = moves
                best_order = list(order)
        else:
            
            current_order = list(order)
            current_moves = 0
            
            temp_order = current_order[:]
            
            while True:
                is_coprime_found = False
                new_order = []
                for i in range(len(temp_order)):
                    new_order.append(temp_order[i])
                    if gcd(temp_order[i], temp_order[(i+1) % len(temp_order)]) == 1:
                        lcm = (temp_order[i] * temp_order[(i+1) % len(temp_order)]) // gcd(temp_order[i], temp_order[(i+1) % len(temp_order)])
                        new_order.append(lcm)
                        current_moves += 1
                        is_coprime_found = True
                temp_order = new_order[:]
                if not is_coprime_found:
                    break
            
            
            is_valid_after_moves = True
            for i in range(len(temp_order)):
                if gcd(temp_order[i], temp_order[(i+1) % len(temp_order)]) == 1:
                    is_valid_after_moves = False
                    break
                    
            if is_valid_after_moves:
                if current_moves < min_moves:
                    min_moves = current_moves
                    best_order = list(order)
            

    print(*best_order)
    print(min_moves)


t = int(input())
for _ in range(t):
    solve()