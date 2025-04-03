def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    coins = 0
    balance = 0
    
    for i in range(n):
        if a[i] > 0:
            balance += a[i]
        elif a[i] < 0:
            if balance >= abs(a[i]):
                balance += a[i]
            else:
                coins += abs(a[i]) - balance
                balance = 0
    print(coins)

t = int(input())
for _ in range(t):
    solve()