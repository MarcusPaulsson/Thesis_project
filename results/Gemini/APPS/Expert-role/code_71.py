def solve():
    n = int(input())
    a = list(map(int, input().split()))

    coins = 0
    balance = 0
    for i in range(n):
        balance += a[i]
        if balance < 0:
            coins += abs(balance)
    print(coins)

t = int(input())
for _ in range(t):
    solve()