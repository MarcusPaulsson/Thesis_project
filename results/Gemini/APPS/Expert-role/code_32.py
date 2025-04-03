def solve():
    n = int(input())
    chanek_coins = 0
    turn = 0
    while n > 0:
        if turn == 0:
            if n % 2 == 0 and n // 2 > 1:
                chanek_coins += n // 2
                n -= n // 2
            else:
                chanek_coins += 1
                n -= 1
        else:
            if n % 2 == 0 and n // 2 > 1:
                n -= n // 2
            else:
                n -= 1
        turn = 1 - turn
    print(chanek_coins)

t = int(input())
for _ in range(t):
    solve()