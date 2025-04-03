def solve():
    n = int(input())
    chanek_coins = 0
    turn = 0 
    
    while n > 0:
        if turn == 0:
            if n % 2 == 0 and n // 2 > 1:
                n_take_half = solve_rec(n // 2, 1)
                n_take_one = solve_rec(n - 1, 1)
                
                if n // 2 + n_take_half >= 1 + n_take_one:
                    chanek_coins += n // 2
                    n -= n // 2
                else:
                    chanek_coins += 1
                    n -= 1
            elif n % 2 == 0:
                chanek_coins += n // 2
                n -= n // 2
            else:
                chanek_coins += 1
                n -= 1
            turn = 1
        else:
            if n % 2 == 0 and n // 2 > 1:
                n_take_half = solve_rec(n // 2, 0)
                n_take_one = solve_rec(n - 1, 0)
                
                if n // 2 + n_take_half >= 1 + n_take_one:
                    n -= n // 2
                else:
                    n -= 1
            elif n % 2 == 0:
                n -= n // 2
            else:
                n -= 1
            turn = 0
            
    print(chanek_coins)
    
def solve_rec(n, turn):
    if n <= 0:
        return 0

    if turn == 0:
        if n % 2 == 0 and n // 2 > 1:
            return max(n // 2  + solve_rec(n // 2, 1), 1 + solve_rec(n - 1, 1))
        elif n % 2 == 0:
            return n // 2 + solve_rec(n // 2, 1)
        else:
            return 1 + solve_rec(n - 1, 1)
    else:
        if n % 2 == 0 and n // 2 > 1:
            return solve_rec(n // 2, 0) if solve_rec(n // 2, 0) > solve_rec(n - 1, 0) else solve_rec(n - 1, 0)
        elif n % 2 == 0:
            return solve_rec(n // 2, 0)
        else:
            return solve_rec(n - 1, 0)

t = int(input())
for _ in range(t):
    solve()