def solve():
    n = int(input())
    chanek_coins = 0
    turn = True  # True for Chanek, False for opponent
    
    while n > 0:
        if n % 2 == 0:
            if (n // 2) >= 1:
                if turn:
                    chanek_coins += (n // 2)
                n //= 2
            else:
                if turn:
                    chanek_coins += 1
                n -= 1
        else:
            if turn:
                chanek_coins += 1
            n -= 1
        turn = not turn
    
    print(chanek_coins)

t = int(input())
for _ in range(t):
    solve()