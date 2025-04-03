def solve():
    n = int(input())
    chanek_coins = 0
    turn = True  # True for Chanek, False for opponent
    
    while n > 0:
        if n % 2 == 0:
            if n == 2:
                move = 1
            else:
                if (n // 2) % 2 == 0 or (n // 2) == 1:
                    move = n // 2
                else:
                    move = 1
        else:
            move = 1
            
        if turn:
            chanek_coins += move
        
        n -= move
        turn = not turn
        
    print(chanek_coins)

t = int(input())
for _ in range(t):
    solve()